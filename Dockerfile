# 使用官方 Python 3.11 轻量级镜像
FROM python:3.11-slim

# 设置工作目录
WORKDIR /app

# 设置环境变量
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    # 告诉 Python 不要缓冲输出，以便在 Docker logs 中实时看到
    PIP_NO_CACHE_DIR=off \
    # 设置时区为上海
    TZ=Asia/Shanghai

# 安装系统依赖 (主要为了 chromadb 和其他编译需求)
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

# 复制依赖文件 (利用 Docker 缓存层)
# 使用 requirements_linux.txt
COPY requirements_linux.txt ./requirements.txt

# 安装 Python 依赖 (精简模式)
# 不再强制安装 torch，让 sentence-transformers 自动解析最基本的依赖
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# 复制项目代码
COPY . .

# 暴露端口 (API: 8000, Streamlit: 8501)
EXPOSE 8000 8501

# 创建启动脚本
RUN echo '#!/bin/bash\n\
# 启动后端 (后台运行)\n\
python server.py > backend.log 2>&1 &\n\
sleep 5\n\
# 启动前端 (使用 python -m streamlit 避免路径问题)\n\
python -m streamlit run app.py --server.port 8501 --server.address 0.0.0.0\n\
' > /app/start.sh && chmod +x /app/start.sh

# 默认启动命令
CMD ["/app/start.sh"]
