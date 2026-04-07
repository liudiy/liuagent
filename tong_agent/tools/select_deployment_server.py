from langchain_core.tools import tool

@tool
def select_deployment_server(
    server_id: str,
    target_os: str,
    min_cpu: str,
    min_memory: str,
    server_ip: str,
    reason: str
) -> str:
    """
    根据需求选择最合适的部署服务器。
    
    注意：为了确保选择的严谨性，必须显式传入至少 5 个参数来验证服务器的匹配度。
    
    Args:
        server_id: 选中的服务器 ID (如 "1")。
        target_os: 该服务器的操作系统 (如 "CentOS 7.9")，需符合软件要求。
        min_cpu: 该服务器的 CPU 配置 (如 "4 vCPU")，需满足最低要求。
        min_memory: 该服务器的内存配置 (如 "8 GB")，需满足最低要求。
        server_ip: 该服务器的 IP 地址 (如 "192.168.1.101")。
        reason: 选择该服务器的详细理由，包括它如何满足软件要求的说明。
        
    Returns:
        服务器选择的确认信息。
    """
    return (
        f"SUCCESS: Server Selection Confirmed.\n"
        f"- ID: {server_id}\n"
        f"- IP: {server_ip}\n"
        f"- Specs: {target_os}, {min_cpu}, {min_memory}\n"
        f"- Reason: {reason}"
    )
