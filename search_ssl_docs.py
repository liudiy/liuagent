import pickle
import os
import re

DOCSTORE_PATH = r"C:\Users\79753\OneDrive\Desktop\TongAgent_langgraph\chroma_db_tongdata_v4_parent_child\docstore.pkl"

if not os.path.exists(DOCSTORE_PATH):
    print("Docstore not found!")
    exit()

with open(DOCSTORE_PATH, "rb") as f:
    docstore = pickle.load(f)

print("Searching for 'SSL' or 'HTTPS' or '证书' or '加密' in docstore...")

tongweb_ssl = []
tongrds_ssl = []

for k, doc in docstore.items():
    content = doc.page_content.lower()
    source = doc.metadata.get('source', '').lower()
    
    if "ssl" in content or "https" in content or "证书" in content or "加密" in content:
        if "tongweb" in content or "tongweb" in source:
            tongweb_ssl.append((doc.metadata.get('source', 'Unknown'), doc.page_content))
        if "tongrds" in content or "rds" in source:
            tongrds_ssl.append((doc.metadata.get('source', 'Unknown'), doc.page_content))

print(f"Found {len(tongweb_ssl)} snippets for TongWeb SSL")
print(f"Found {len(tongrds_ssl)} snippets for TongRDS SSL")

if tongweb_ssl:
    print("\n--- TongWeb SSL Snippet ---")
    for src, text in tongweb_ssl[:3]:
        print(f"Source: {src}")
        print(text[:300].replace('\n', ' '))
        print("-" * 40)

if tongrds_ssl:
    print("\n--- TongRDS SSL Snippet ---")
    for src, text in tongrds_ssl[:3]:
        print(f"Source: {src}")
        print(text[:300].replace('\n', ' '))
        print("-" * 40)
