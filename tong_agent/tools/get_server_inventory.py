import os
import re
from langchain_core.tools import tool

@tool
def get_server_inventory(filter_query: str = None) -> str:
    """
    查询服务器库存文件 (server_inventory_mock.md)。
    由于文件包含 100,000+ 台服务器，**必须**提供筛选条件，否则默认只返回前 5 条。
    
    Args:
        filter_query: 筛选条件，支持简单的关键词匹配（例如："CentOS", "32", "Running"）。
                      多个关键词用空格分隔，表示 AND 关系。
                      注意：CPU和内存请直接搜索数字（如搜 "16" 而不是 "16GB"），工具会自动忽略单位。
    
    Returns:
        符合条件的服务器列表（Markdown 表格格式，最多返回 10 条，并包含总数提示）。
        每个服务器包含 10 个参数：ID, Hostname, IP, OS, CPU, Memory, Disk, Bandwidth, Zone, Status。
    """
    file_path = os.path.join(os.getcwd(), "server_inventory_mock.md")
    
    if not os.path.exists(file_path):
        return "Error: server_inventory_mock.md not found."
        
    results = []
    header_line = ""
    separator_line = ""
    
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            # Read header
            header_line = f.readline()
            separator_line = f.readline()
            
            # Smart keyword filtering
            keywords = []
            if filter_query:
                # Pre-process query: remove common units from numbers to match raw data
                # e.g., "16GB" -> "16", "8Cores" -> "8"
                raw_keywords = filter_query.lower().split()
                for kw in raw_keywords:
                    # Remove 'gb', 'mb', 'tb', 'core', 'cores', 'v' (for vcpu) suffix from numbers
                    clean_kw = re.sub(r'(\d+)(gb|mb|tb|g|m|t|core|cores|v|vcpu)', r'\1', kw)
                    keywords.append(clean_kw)
            
            # Scan file line by line
            count = 0
            for line in f:
                if not line.strip():
                    continue
                    
                line_lower = line.lower()
                match = True
                for kw in keywords:
                    if kw not in line_lower:
                        match = False
                        break
                
                if match:
                    count += 1
                    # Only collect top 10 results to save memory
                    if len(results) < 10:
                        results.append(line)
                
                # Performance safety break (optional)
                # If we have found 10 results, we could stop if we don't care about total count.
                # But calculating total count is useful for the user context.
                # Since we are just counting integer matches, it's fast.
                pass
    except Exception as e:
        return f"Error reading inventory file: {e}"

    # Format output
    # count is the total number of matches found in the file
    
    display_results = results # This is already max 10
    
    msg = ""
    if not filter_query:
        msg = f"Warning: No filter provided. Scanned {count} servers. Showing top {len(display_results)}."
    else:
        if not display_results:
            msg = f"No servers found matching query: '{filter_query}'."
        else:
            msg = f"Found {count} matches for '{filter_query}'. Showing top {len(display_results)} results."

    output = f"{msg}\n\n"
    output += header_line
    output += separator_line
    output += "".join(display_results)
    
    return output
