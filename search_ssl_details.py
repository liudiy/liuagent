import pickle
import os
import re

DOCSTORE_PATH = r"C:\Users\79753\OneDrive\Desktop\TongAgent_langgraph\chroma_db_tongdata_v4_parent_child\docstore.pkl"

with open(DOCSTORE_PATH, "rb") as f:
    docstore = pickle.load(f)

for k, doc in docstore.items():
    content = doc.page_content
    source = doc.metadata.get('source', '').lower()
    
    if "tongrds" in source and "Server.Listen.Secure" in content:
        print(f"--- TongRDS Config ---")
        print(source)
        print(content)
        print("-" * 40)
        
    if "tongweb" in source and "ssl" in content.lower() and "通道" in content and "https" in content.lower():
        if len(content) < 800:
            print(f"--- TongWeb Config ---")
            print(source)
            print(content[:300])
            print("-" * 40)
