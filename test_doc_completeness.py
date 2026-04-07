import pickle
import os

DOCSTORE_PATH = r"C:\Users\79753\OneDrive\Desktop\TongAgent_langgraph\chroma_db_tongdata_v4_parent_child\docstore.pkl"

if not os.path.exists(DOCSTORE_PATH):
    print("Docstore not found!")
    exit()

with open(DOCSTORE_PATH, "rb") as f:
    docstore = pickle.load(f)

print("Searching for 'keepalived' in TongHttpServer docs...")
keepalived_found = False
for k, doc in docstore.items():
    content = doc.page_content.lower()
    if "keepalived" in content:
        keepalived_found = True
        print(f"\n[FOUND Keepalived in {doc.metadata.get('source', 'Unknown')}]")
        print(doc.page_content[:300].replace('\n', ' '))
        break

print("\nSearching for '内存数据库' or 'redis' in TongRDS docs...")
rds_memory_found = False
for k, doc in docstore.items():
    content = doc.page_content.lower()
    if "tongrds" in content and ("内存数据" in content or "redis" in content):
        rds_memory_found = True
        print(f"\n[FOUND Memory DB in {doc.metadata.get('source', 'Unknown')}]")
        print(doc.page_content[:300].replace('\n', ' '))
        break # Just need to confirm it exists