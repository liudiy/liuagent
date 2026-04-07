import os
import sys

# 尝试加载 langchain_chroma
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

BASE_DIR = os.path.dirname(__file__)
CHROMA_DB_PATH = os.path.join(BASE_DIR, "chroma_db_tongdata_v2")

def check_db():
    embeddings = HuggingFaceEmbeddings(
        model_name=os.path.join(BASE_DIR, "bge-large-zh-v1.5"),
        model_kwargs={'device': 'cpu'},
        encode_kwargs={'normalize_embeddings': True}
    )
    vectorstore = Chroma(
        persist_directory=CHROMA_DB_PATH,
        embedding_function=embeddings
    )
    
    docs = vectorstore.similarity_search("怎么部署tongweb", k=5)
    for i, doc in enumerate(docs):
        print(f"[{i}] Source: {doc.metadata.get('source')}")
        print(f"Content: {doc.page_content[:200]}...\n")

if __name__ == "__main__":
    check_db()
