import os
import sys

from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

BASE_DIR = os.path.dirname(__file__)
CHROMA_DB_PATH = os.path.join(BASE_DIR, "chroma_db_tongdata_v2")

def check_db_sources():
    embeddings = HuggingFaceEmbeddings(
        model_name=os.path.join(BASE_DIR, "bge-large-zh-v1.5"),
        model_kwargs={'device': 'cpu'},
        encode_kwargs={'normalize_embeddings': True}
    )
    vectorstore = Chroma(
        persist_directory=CHROMA_DB_PATH,
        embedding_function=embeddings
    )
    
    data = vectorstore.get()
    sources = set()
    for meta in data.get('metadatas', []):
        if meta and 'source' in meta:
            sources.add(os.path.basename(meta['source']))
    
    print("Documents in Vector DB:")
    for s in sources:
        print("-", s)

if __name__ == "__main__":
    check_db_sources()
