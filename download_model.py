import os
# 设置国内镜像源
os.environ["HF_ENDPOINT"] = "https://hf-mirror.com"

from huggingface_hub import snapshot_download

print("开始下载 BAAI/bge-large-zh-v1.5 模型到本地文件夹...")
snapshot_download(
    repo_id="BAAI/bge-large-zh-v1.5",
    local_dir="bge-large-zh-v1.5",
    local_dir_use_symlinks=False,
    resume_download=True
)
print("模型下载完成！")