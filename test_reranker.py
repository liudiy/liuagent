from sentence_transformers import CrossEncoder
import os

print("Checking HF Hub cache...")
cache_dir = os.path.expanduser("~/.cache/huggingface/hub/models--BAAI--bge-reranker-v2-m3")
if os.path.exists(cache_dir):
    print(f"Cache dir exists: {cache_dir}")
else:
    print(f"Cache dir does NOT exist: {cache_dir}")

print("\nTrying to load model...")
os.environ["HF_ENDPOINT"] = "https://hf-mirror.com"
try:
    model = CrossEncoder("BAAI/bge-reranker-v2-m3", device="cpu", local_files_only=True)
    print("Model loaded successfully from local files.")
except Exception as e:
    print(f"Failed to load with local_files_only=True: {e}")
    print("Trying without local_files_only...")
    try:
        model = CrossEncoder("BAAI/bge-reranker-v2-m3", device="cpu")
        print("Model loaded successfully from remote/cache.")
    except Exception as e2:
        print(f"Failed to load completely: {e2}")
