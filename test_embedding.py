import os
import shutil
import stat
from huggingface_hub import snapshot_download
from langchain_huggingface import HuggingFaceEmbeddings

def remove_readonly(func, path, excinfo):
    try:
        os.chmod(path, stat.S_IWRITE)
        func(path)
    except Exception as e:
        pass

local_model_dir = os.path.abspath("./bge-m3")

print(f"正在清理本地模型目录: {local_model_dir}")
if os.path.exists(local_model_dir):
    shutil.rmtree(local_model_dir, onerror=remove_readonly)
    print("目录清理完成。")

# 强制禁用代理，并使用国内镜像
os.environ.pop("HTTP_PROXY", None)
os.environ.pop("HTTPS_PROXY", None)
os.environ.pop("http_proxy", None)
os.environ.pop("https_proxy", None)
os.environ.pop("ALL_PROXY", None)
os.environ.pop("all_proxy", None)

os.environ["HF_ENDPOINT"] = "https://hf-mirror.com"

print("正在通过 hf-mirror 重新下载核心模型文件到本地目录...")
try:
    # 使用 local_dir 避免 Windows 下的 symlink 问题
    model_path = snapshot_download(
        repo_id="BAAI/bge-m3", 
        local_dir=local_model_dir,
        local_dir_use_symlinks=False, # 强制不使用符号链接
        resume_download=True,
        allow_patterns=[
            "*.json", 
            "*.bin", 
            "*.model", 
            "*.pt",
            "1_Pooling/*"
        ],
        ignore_patterns=["onnx/*", "imgs/*"]
    )
    print(f"模型文件已成功下载到: {model_path}")
except Exception as e:
    print(f"模型下载失败: {e}")
    model_path = local_model_dir

print("正在加载模型...")
try:
    embeddings = HuggingFaceEmbeddings(
        model_name=model_path,
        model_kwargs={'device': 'cuda'},
        encode_kwargs={'normalize_embeddings': True}
    )
    print("模型加载成功！测试向量化...")
    vec = embeddings.embed_query("这是一个测试句子。")
    print(f"向量化成功！向量维度: {len(vec)}")
except Exception as e:
    print(f"加载或测试失败: {e}")
    import traceback
    traceback.print_exc()
