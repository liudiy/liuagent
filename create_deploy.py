import os
import zipfile

def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        # 跳过一些不需要的目录
        if '__pycache__' in root or '.git' in root or '.pytest_cache' in root:
            continue
        for file in files:
            if file.endswith('.pyc'):
                continue
            file_path = os.path.join(root, file)
            arcname = os.path.relpath(file_path, os.path.dirname(__file__))
            ziph.write(file_path, arcname)

if __name__ == '__main__':
    zip_filename = 'deploy_package_with_model.zip'
    print(f"正在打包 {zip_filename}，由于包含了模型文件，这可能需要几分钟时间...")
    
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # 添加单个文件
        files_to_add = ['app.py', 'server.py', 'requirements.txt', 'requirements_linux.txt', 'Dockerfile', 'docker-compose.yml', '.env', 'bm25_retriever.pkl']
        for f in files_to_add:
            if os.path.exists(f):
                zipf.write(f)
                
        # 添加目录
        dirs_to_add = ['tong_agent', 'chroma_db_tongdata_v2', 'bge-large-zh-v1.5']
        for d in dirs_to_add:
            if os.path.exists(d):
                zipdir(d, zipf)
                
    print("打包完成！")
