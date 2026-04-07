import os
import shutil

# 强制设置 HuggingFace 国内镜像源
os.environ["HF_ENDPOINT"] = "https://hf-mirror.com"

from huggingface_hub import snapshot_download
from langchain_huggingface import HuggingFaceEmbeddings

model_id = "BAAI/bge-m3"

print(f"正在通过镜像源重新下载并修复模型: {model_id} ...")
try:
    # 我们只下载核心的模型权重和配置文件，精确忽略那些导致 403 错误的图片和无用文件
    model_path = snapshot_download(
        repo_id=model_id, 
        force_download=False,
        ignore_patterns=["imgs/*", "*.jpg", "*.webp", "*.png", "*.DS_Store"]
    )
    print(f"✅ 模型文件已成功下载，保存在: {model_path}")
    
    # 发现缺少了 config_sentence_transformers.json，这可能不是由 BAAI/bge-m3 官方仓库提供的
    # BGE-M3 本质是一个 AutoModel，我们用 sentence-transformers 加载时有时需要补充生成配置文件
    import json
    config_path = os.path.join(model_path, "config_sentence_transformers.json")
    if not os.path.exists(config_path):
        print(f"⚠️ 未找到 config_sentence_transformers.json，正在手动生成...")
        config_data = {
            "__version__": "2.2.2",
            "sentence_transformer_type": "sentence_transformers.models.Transformer"
        }
        with open(config_path, "w", encoding="utf-8") as f:
            json.dump(config_data, f)
            
    modules_path = os.path.join(model_path, "modules.json")
    if not os.path.exists(modules_path):
        print(f"⚠️ 未找到 modules.json，正在手动生成...")
        modules_data = [
            {
                "idx": 0,
                "name": "0",
                "path": "",
                "type": "sentence_transformers.models.Transformer"
            },
            {
                "idx": 1,
                "name": "1",
                "path": "1_Pooling",
                "type": "sentence_transformers.models.Pooling"
            }
        ]
        with open(modules_path, "w", encoding="utf-8") as f:
            json.dump(modules_data, f)
            
    pooling_dir = os.path.join(model_path, "1_Pooling")
    if not os.path.exists(pooling_dir):
        os.makedirs(pooling_dir)
        pooling_config_path = os.path.join(pooling_dir, "config.json")
        pooling_data = {
            "word_embedding_dimension": 1024,
            "pooling_mode_cls_token": True,
            "pooling_mode_mean_tokens": False,
            "pooling_mode_max_tokens": False,
            "pooling_mode_mean_sqrt_len_tokens": False,
            "pooling_mode_weightedmean_tokens": False,
            "pooling_mode_lasttoken": False
        }
        with open(pooling_config_path, "w", encoding="utf-8") as f:
            json.dump(pooling_data, f)
            
    sentence_bert_config_path = os.path.join(model_path, "sentence_bert_config.json")
    if not os.path.exists(sentence_bert_config_path):
        print(f"⚠️ 未找到 sentence_bert_config.json，正在手动生成...")
        sentence_bert_data = {
            "max_seq_length": 8192,
            "do_lower_case": False
        }
        with open(sentence_bert_config_path, "w", encoding="utf-8") as f:
            json.dump(sentence_bert_data, f)
            
    print("正在尝试将模型加载到显存进行验证...")
    embeddings = HuggingFaceEmbeddings(
        model_name=model_path,
        model_kwargs={'device': 'cuda'}, 
        encode_kwargs={'normalize_embeddings': True} 
    )
    # 随便计算一个向量，确保模型真的可以工作
    vector = embeddings.embed_query("测试验证文本")
    print(f"✅ 验证成功！模型可以正常工作。测试向量维度: {len(vector)}")
    
except Exception as e:
    print(f"❌ 下载或加载失败: {e}")
