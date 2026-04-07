import pickle
import os

DOCSTORE_PATH = r"C:\Users\79753\OneDrive\Desktop\TongAgent_langgraph\chroma_db_tongdata_v4_parent_child\docstore.pkl"

if not os.path.exists(DOCSTORE_PATH):
    print(f"Error: {DOCSTORE_PATH} does not exist.")
    exit(1)

with open(DOCSTORE_PATH, "rb") as f:
    docstore = pickle.load(f)

print(f"Total documents in docstore: {len(docstore.items())}")

ths_docs = []
tongweb_docs = []

for k, doc in docstore.items():
    content = doc.page_content.lower()
    
    if "tonghttpserver" in content or "ths" in content:
        if "定义" in content or "集群" in content or "架构" in content:
            ths_docs.append(doc.page_content)
            
    if "tongweb" in content:
        if "定义" in content or "集群" in content or "架构" in content:
            tongweb_docs.append(doc.page_content)

print(f"\n--- TongHttpServer 相关文档 (带定义/集群/架构) 数量: {len(ths_docs)} ---")
if ths_docs:
    print("预览前2个:")
    for i, d in enumerate(ths_docs[:2]):
        print(f"\n[{i+1}] {d[:300]}...")

print(f"\n--- TongWeb 相关文档 (带定义/集群/架构) 数量: {len(tongweb_docs)} ---")
if tongweb_docs:
    print("预览前2个:")
    for i, d in enumerate(tongweb_docs[:2]):
        print(f"\n[{i+1}] {d[:300]}...")
