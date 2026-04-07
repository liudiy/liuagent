import pickle
import os

DOCSTORE_PATH = r"C:\Users\79753\OneDrive\Desktop\TongAgent_langgraph\chroma_db_tongdata_v4_parent_child\docstore.pkl"

if not os.path.exists(DOCSTORE_PATH):
    print("Docstore not found!")
    exit()

with open(DOCSTORE_PATH, "rb") as f:
    docstore = pickle.load(f)

ths_ssl = ""
tw_ssl = ""
rds_ssl = ""

for k, doc in docstore.items():
    content = doc.page_content
    source = doc.metadata.get('source', '').lower()
    
    # Extract TongHttpServer SSL config
    if "ths" in source or "tonghttpserver" in source:
        if "ssl_certificate" in content or "ssl_protocols" in content:
            if not ths_ssl:
                ths_ssl = f"【来源文件】: {doc.metadata.get('source')}\n" + content
                
    # Extract TongWeb SSL config
    if "tongweb" in source:
        if "开启 SSL" in content or "ssl-enabled=\"true\"" in content:
            if not tw_ssl:
                tw_ssl = f"【来源文件】: {doc.metadata.get('source')}\n" + content
                
    # Extract TongRDS SSL config
    if "tongrds" in source or "rds" in source:
        if "Server.Listen.Secure" in content or "SslCiphers" in content:
            if not rds_ssl:
                rds_ssl = f"【来源文件】: {doc.metadata.get('source')}\n" + content

print("=== TongHttpServer (THS) SSL 配置方法 ===")
print(ths_ssl[:1000] if ths_ssl else "未在本地知识库找到具体配置")

print("\n\n=== TongWeb (TW) SSL 配置方法 ===")
print(tw_ssl[:1000] if tw_ssl else "未在本地知识库找到具体配置")

print("\n\n=== TongRDS (TRDS) SSL 配置方法 ===")
print(rds_ssl[:1000] if rds_ssl else "未在本地知识库找到具体配置")
