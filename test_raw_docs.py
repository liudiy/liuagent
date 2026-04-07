import pickle
import re

DOCSTORE_PATH = r"C:\Users\79753\OneDrive\Desktop\TongAgent_langgraph\chroma_db_tongdata_v4_parent_child\docstore.pkl"

with open(DOCSTORE_PATH, "rb") as f:
    docstore = pickle.load(f)

rds_content = ""
ths_content = ""

for k, doc in docstore.items():
    src = doc.metadata.get('source', '')
    if "TongRDS" in src:
        rds_content += doc.page_content + "\n"
    elif "TongHttpServer" in src:
        ths_content += doc.page_content + "\n"

print(f"Total TongRDS doc size: {len(rds_content)} chars")
print(f"Total TongHttpServer doc size: {len(ths_content)} chars")

print("\n--- Searching TongRDS for Hardware/CPU/Memory/RAM ---")
hardware_patterns = [r'\d+\s*[Gg][Bb]', r'\d+\s*核', r'内存', r'CPU']
for p in hardware_patterns:
    matches = re.finditer(p, rds_content, re.IGNORECASE)
    count = 0
    for m in matches:
        start = max(0, m.start() - 30)
        end = min(len(rds_content), m.end() + 30)
        print(f"Found '{p}': ...{rds_content[start:end].replace(chr(10), ' ')}...")
        count += 1
        if count > 3: break # show first few

print("\n--- Searching TongHttpServer for Hardware/CPU/Memory/RAM ---")
for p in hardware_patterns:
    matches = re.finditer(p, ths_content, re.IGNORECASE)
    count = 0
    for m in matches:
        start = max(0, m.start() - 30)
        end = min(len(ths_content), m.end() + 30)
        print(f"Found '{p}': ...{ths_content[start:end].replace(chr(10), ' ')}...")
        count += 1
        if count > 3: break
