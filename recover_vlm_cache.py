import os
import pickle
from dotenv import load_dotenv

load_dotenv()
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CHROMA_DB_PATH = os.path.join(BASE_DIR, "chroma_db_tongdata_v4_parent_child")
STORE_PATH = os.path.join(CHROMA_DB_PATH, "docstore.pkl")
CHUNKING_CHECKPOINT = os.path.join(BASE_DIR, "vlm_chunking_cache.pkl")

def recover_chunks():
    print("🔍 正在从向量库本地存储 (docstore.pkl) 中捞回之前切分好的数据...")
    if not os.path.exists(STORE_PATH):
        print("❌ 找不到 docstore.pkl！")
        return

    with open(STORE_PATH, "rb") as f:
        store_dict = pickle.load(f)
        
    print(f"📦 发现 {len(store_dict)} 个文档记录。")
    
    # 筛选出属于 VLM 提取的那些高质量表格/图片文档 (根据我们打的 metadata 标记)
    vlm_chunks = []
    for doc_id, doc in store_dict.items():
        if doc and hasattr(doc, 'metadata'):
            # 我们在代码里给 VLM 提取的内容打了 type="vlm_extracted" 或 type="vlm_enhanced"
            if doc.metadata.get("type") in ["vlm_extracted", "vlm_enhanced"]:
                vlm_chunks.append(doc)
                
    print(f"🎯 成功筛选出 {len(vlm_chunks)} 个包含图表的多模态文档块！")
    
    if vlm_chunks:
        print("💾 正在将它们保存为本地缓存文件 (vlm_chunking_cache.pkl)...")
        with open(CHUNKING_CHECKPOINT, 'wb') as f:
            pickle.dump(vlm_chunks, f)
        print("✅ 恢复成功！现在您可以直接运行 python ingest_multimodal_data.py 了！")
    else:
        print("⚠️ 未找到任何带有 vlm 标记的文档，说明之前的向量库写入可能因为报错完全回滚了。您需要重新跑一遍。")

if __name__ == "__main__":
    recover_chunks()
