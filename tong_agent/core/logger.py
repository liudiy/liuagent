import logging
import sys
from logging.handlers import RotatingFileHandler

def setup_logger(name: str = "TongAgent"):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # 避免重复添加 Handler
    if not logger.handlers:
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )

        # 控制台输出
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.INFO) # 终端只看 INFO 及以上
        console_handler.setFormatter(formatter)

        # 文件输出 (按大小滚动，最大 5MB，保留 3 个备份)
        file_handler = RotatingFileHandler(
            'agent_run.log', maxBytes=5*1024*1024, backupCount=3, encoding='utf-8'
        )
        file_handler.setLevel(logging.DEBUG) # 文件里记录所有细节
        file_handler.setFormatter(formatter)

        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

    return logger

def get_logger(name: str = "TongAgent"):
    return setup_logger(name)

logger = get_logger()
