import random
import uuid
import os

def generate_mock_servers(filename="server_inventory_mock.md", count=100000):
    print(f"Generating {count} mock servers to {filename}...")
    
    # 10 parameters
    headers = ["ID", "Hostname", "IP Address", "OS", "CPU (Cores)", "Memory (GB)", "Disk (TB)", "Bandwidth (Gbps)", "Zone", "Status"]
    
    os_versions = ["CentOS 7.9", "Ubuntu 20.04 LTS", "Windows Server 2019", "Red Hat Enterprise Linux 8", "Debian 11"]
    zones = ["cn-beijing-a", "cn-beijing-b", "cn-shanghai-a", "cn-hangzhou-b"]
    statuses = ["Active", "Maintenance", "Offline", "Provisioning"]
    
    with open(filename, "w", encoding="utf-8") as f:
        # Write Markdown Table Header
        f.write("| " + " | ".join(headers) + " |\n")
        f.write("| " + " | ".join(["---"] * len(headers)) + " |\n")
        
        for i in range(count):
            srv_id = str(uuid.uuid4())[:8]
            hostname = f"srv-{i:06d}"
            ip = f"192.168.{random.randint(1, 254)}.{random.randint(1, 254)}"
            os_ver = random.choice(os_versions)
            cpu = str(random.choice([4, 8, 16, 32, 64, 96]))
            mem = str(random.choice([16, 32, 64, 128, 256, 512]))
            disk = str(random.choice([1, 2, 4, 8, 10, 20]))
            bw = str(random.choice([1, 10, 25, 40, 100]))
            zone = random.choice(zones)
            status = random.choice(statuses)
            
            row = [srv_id, hostname, ip, os_ver, cpu, mem, disk, bw, zone, status]
            f.write("| " + " | ".join(row) + " |\n")
            
            if (i + 1) % 10000 == 0:
                print(f"Generated {i + 1} rows...")
                
    print("Done!")

if __name__ == "__main__":
    generate_mock_servers()
