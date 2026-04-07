from tong_agent.tools.file_tools import list_directory, search_file_content, read_file_content, glob_files

# ==========================================
# 工具注册表 (Tools Registry)
# ==========================================

tools = [
    list_directory,
    search_file_content,
    read_file_content,
    glob_files,
]

tool_map = {tool.name: tool for tool in tools}
