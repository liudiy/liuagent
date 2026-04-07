import json
import random
from dataclasses import dataclass, asdict

# --- 1. 定义东方通软件的参数要求 (Mock Requirements) ---
# 假设我们要部署 TongWeb 7.0
REQUIRED_CONFIG = {
    "os_type": "Linux",          # 必须是 Linux
    "cpu_cores": 4,              # 至少 4 核
    "memory_gb": 8,              # 至少 8 GB 内存
    "disk_space_gb": 50,         # 至少 50 GB 磁盘空间
    "jdk_version": "1.8"         # 必须是 JDK 1.8 或更高
}

# --- 2. 定义服务器数据结构 ---
@dataclass
class Server:
    server_id: str
    ip_address: str
    os_type: str
    cpu_cores: int
    memory_gb: int
    disk_space_gb: int
    jdk_version: str

# --- 3. 随机生成 500 台服务器数据 ---
def generate_mock_servers(count=500):
    servers = []
    
    # 预定义一些可选值，模拟真实环境的多样性
    os_choices = ["Linux", "Windows Server", "CentOS", "Ubuntu", "RedHat"]
    cpu_choices = [2, 4, 8, 16, 32]
    memory_choices = [4, 8, 16, 32, 64, 128]
    disk_choices = [20, 50, 100, 200, 500]
    jdk_choices = ["1.7", "1.8", "11", "17", "None"]

    for i in range(1, count + 1):
        # 故意制造一些不满足条件的服务器
        # 比如：大部分是 Linux，但也有 Windows
        os_type = random.choice(os_choices)
        
        # CPU 和 内存 随机
        cpu = random.choice(cpu_choices)
        memory = random.choice(memory_choices)
        disk = random.choice(disk_choices)
        jdk = random.choice(jdk_choices)

        server = Server(
            server_id=f"srv-{i:03d}",
            ip_address=f"192.168.1.{i%255}",
            os_type=os_type,
            cpu_cores=cpu,
            memory_gb=memory,
            disk_space_gb=disk,
            jdk_version=jdk
        )
        servers.append(asdict(server))
    
    return servers

# --- 4. 执行生成并保存到文件 ---
if __name__ == "__main__":
    servers = generate_mock_servers(500)
    
    # 保存为 JSON 文件，方便 Agent 读取
    file_path = "mock_server_inventory.json"
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(servers, f, indent=2, ensure_ascii=False)
    
    print(f"✅ 已生成 {len(servers)} 台模拟服务器数据，保存在: {file_path}")
    print("\n--- 示例数据 (前 3 台) ---")
    print(json.dumps(servers[:3], indent=2, ensure_ascii=False))
    
    # 同时把需求也保存一下，方便参考
    with open("tongweb_requirements.json", "w", encoding="utf-8") as f:
        json.dump(REQUIRED_CONFIG, f, indent=2, ensure_ascii=False)
    print("\n✅ 软件参数要求已保存: tongweb_requirements.json")
