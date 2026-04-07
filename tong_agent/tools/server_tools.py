import json
import os
from langchain_core.tools import tool
from typing import List, Dict, Union

# @tool
# def get_server_inventory() -> str:
#     """
#     获取当前所有服务器的库存列表。
#     注意：由于数据量较大（500台+），此工具不会直接返回 JSON 数据，而是会返回存储数据的本地文件路径。
#     请使用 Python 代码读取该文件进行分析。
#     """
#     file_path = os.path.abspath("mock_server_inventory.json")
#     
#     if not os.path.exists(file_path):
#         # 如果文件不存在，尝试生成一份模拟数据（仅用于演示）
#         try:
#             # 简单的模拟数据生成逻辑
#             mock_data = []
#             for i in range(1, 501):
#                 mock_data.append({
#                     "server_id": f"srv-{i:03d}",
#                     "ip_address": f"192.168.1.{i}",
#                     "os_type": "Linux" if i % 2 == 0 else "Windows Server",
#                     "cpu_cores": 4 if i % 3 == 0 else 2,
#                     "memory_gb": 8 if i % 3 == 0 else 4,
#                     "disk_space_gb": 100,
#                     "jdk_version": "1.8" if i % 5 == 0 else "None"
#                 })
#             with open(file_path, "w", encoding="utf-8") as f:
#                 json.dump(mock_data, f, ensure_ascii=False, indent=2)
#             return f"已生成并获取 500 台服务器的库存数据。数据已存储在文件中: {file_path}\n请编写 Python 代码，使用 `json` 模块读取此文件并进行筛选分析。"
#         except Exception as e:
#              return f"Error: mock_server_inventory.json not found and failed to create: {str(e)}"
#
#     return f"已获取 500 台服务器的库存数据。由于数据量较大，数据已存储在文件中: {file_path}\n请编写 Python 代码，使用 `json` 模块读取此文件并进行筛选分析。"

# @tool
# def get_tongweb_requirements() -> Dict:
#     """
#     获取 TongWeb 软件的安装环境要求。
#     返回一个字典，包含最低配置要求，如:
#     os_type, cpu_cores, memory_gb, disk_space_gb, jdk_version。
#     """
#     try:
#         with open("tongweb_requirements.json", "r", encoding="utf-8") as f:
#             reqs = json.load(f)
#         return reqs
#     except FileNotFoundError:
#         return {
#             "os_type": "Linux",
#             "cpu_cores": 4,
#             "memory_gb": 8,
#             "disk_space_gb": 50,
#             "jdk_version": "1.8"
#         }
