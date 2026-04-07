import json

# Define the structure for our test cases
test_cases = {
    "test_cases": []
}

# Helper to add cases
def add_cases(category, product, questions, expected_intent="answer"):
    for i, q in enumerate(questions):
        test_cases["test_cases"].append({
            "id": f"{category}_{product}_{i+1}",
            "category": category,
            "product": product,
            "question": q,
            "expected_intent": expected_intent
        })

# --- Category 1: Fact Extraction (事实抽取) ---
# TongWeb 7
tw7_facts = [
    "TongWeb 7 的默认 HTTP 端口是多少？",
    "TongWeb 7 支持的最高 JDK 版本是多少？",
    "如何查看 TongWeb 7 的运行日志？",
    "TongWeb 7 启动失败报端口冲突，应该修改哪个配置文件？",
    "TongWeb 7 如何部署 WAR 包？",
    "TongWeb 7 控制台的默认管理员账号和密码是什么？",
    "TongWeb 7 支持哪些操作系统的安装？",
    "在 Linux 系统下，TongWeb 7 的启动脚本叫什么名字？",
    "TongWeb 7 如何配置虚拟主机？",
    "TongWeb 7 的 session 默认超时时间是多少？",
    "TongWeb 7 能否以 Windows 服务的方式运行？",
    "TongWeb 7 中如何配置数据源连接池？",
    "如何平滑重启 TongWeb 7 节点？",
    "TongWeb 7 的标准安装目录结构是怎样的？",
    "TongWeb 7 如何开启访问日志（Access Log）？"
]
add_cases("fact_extraction", "TongWeb7", tw7_facts)

# TongWeb 8
tw8_facts = [
    "TongWeb 8 相比 TongWeb 7 有哪些核心架构变化？",
    "TongWeb 8 的默认管理控制台端口是多少？",
    "TongWeb 8 如何配置国密算法支持？",
    "TongWeb 8 中如何实现应用的灰度发布？",
    "TongWeb 8 的微服务网关组件如何配置路由？",
    "TongWeb 8 是否原生支持 Spring Boot 应用的无缝迁移？",
    "TongWeb 8 控制台的高可用如何配置？",
    "TongWeb 8 如何通过命令行工具执行部署操作？",
    "TongWeb 8 中线程池的最小和最大线程数在哪里配置？",
    "TongWeb 8 启动时报 OutOfMemoryError，应该修改哪个 JVM 参数文件？",
    "TongWeb 8 如何配置 HTTPS 双向认证？",
    "TongWeb 8 支持动态修改哪些参数而不需要重启服务器？",
    "TongWeb 8 容器的类加载机制是怎样的？",
    "如何配置 TongWeb 8 的 JNDI 数据源？",
    "TongWeb 8 的集群组播地址怎么修改？"
]
add_cases("fact_extraction", "TongWeb8", tw8_facts)

# TongRDS 2
rds_facts = [
    "TongRDS 2 是基于什么开源缓存技术研发的？",
    "TongRDS 2 集群模式下，官方推荐的最小节点数量是多少？",
    "TongRDS 2 如何开启 AOF 持久化？",
    "TongRDS 2 内存淘汰策略有哪些？默认是哪一种？",
    "TongRDS 2 如何修改默认的监听端口 6379？",
    "TongRDS 2 在启动时如何指定配置文件路径？",
    "TongRDS 2 主从同步断开后如何排查？",
    "TongRDS 2 哨兵模式（Sentinel）如何配置？",
    "TongRDS 2 如何设置访问密码？",
    "TongRDS 2 支持哪些数据结构？",
    "如何查看 TongRDS 2 当前的内存使用率？",
    "TongRDS 2 集群增加新节点时，如何进行槽位（Slot）迁移？",
    "TongRDS 2 的 RDB 快照备份如何手动触发？",
    "TongRDS 2 最大支持多大的单实例内存？",
    "TongRDS 2 的慢查询日志（Slowlog）如何配置和查看？"
]
add_cases("fact_extraction", "TongRDS2", rds_facts)

# THS 6 (TongHttpServer)
ths_facts = [
    "THS 6 的底层是基于哪个开源 Web 服务器开发的？",
    "THS 6 的主配置文件名称是什么？",
    "THS 6 如何配置轮询（Round Robin）负载均衡？",
    "THS 6 如何配置对后端 TongWeb 节点的健康检查？",
    "THS 6 启动报错 502 Bad Gateway 的常见原因有哪些？",
    "THS 6 如何配置 IP 访问黑白名单？",
    "THS 6 的日志切割（Logrotate）如何配置？",
    "THS 6 怎么配置 SSL 证书开启 HTTPS？",
    "THS 6 中 worker_processes 参数的建议配置值是多少？",
    "THS 6 如何通过 Keepalived 实现高可用双机热备？",
    "THS 6 配置文件中 upstream 模块的作用是什么？",
    "THS 6 如何限制客户端单 IP 的并发连接数？",
    "THS 6 支持 WebSocket 协议转发吗？如何配置？",
    "THS 6 的缓存功能（Proxy Cache）如何开启？",
    "THS 6 重新加载配置文件的命令是什么？"
]
add_cases("fact_extraction", "THS6", ths_facts)

# --- Category 2: Complex Reasoning & Troubleshooting (复杂推理) ---
complex_cases = [
    # Architecture & Planning
    "我有 4 台 16核 32G 的服务器，要求部署 THS 负载均衡和 TongWeb 业务节点，且两者都要高可用，请给出最优分配方案。",
    "业务系统峰值并发有 10000，使用 TongWeb 8 + TongRDS 2 架构，应该如何评估 TongRDS 的内存容量和 TongWeb 的线程数？",
    "如果我想实现前后端分离，前端静态资源放在 THS，动态请求转发到后端的 TongWeb 集群，THS 的 conf 文件核心应该怎么写？",
    "TongRDS 只有两台物理机，为了防止脑裂，图谱和文档中推荐怎么部署 3主3从？",
    "如何把旧的 Tomcat 应用平滑迁移到 TongWeb 7 上？主要需要注意哪些配置的差异？",
    
    # Troubleshooting & Diagnostics
    "前端用户报告说登录系统总是掉线，需要频繁重新登录。我查看了 THS 的日志一切正常，TongWeb 的 CPU 占用也很低。请问问题可能出在哪里，我该去查哪台机器的什么日志？",
    "THS 控制台一直刷 '[ERR-THS-0019] Connect backend failed'，但是后端 TongWeb 的进程还在，请列出排查此问题的 3 个主要方向。",
    "TongWeb 8 启动时，日志卡在 'Initialize Spring Root WebApplicationContext' 长达 10 分钟，最后报连接超时。可能和外挂的 TongRDS 有关吗？如何排查？",
    "TongRDS 2 的内存使用率突然飙升到 99% 并导致服务 OOM 崩溃。为了定位大 Key，我应该怎么做？",
    "THS 配置了两个 TongWeb 节点 A 和 B。节点 A 宕机后，THS 依然把请求转发给 A 导致大量 502 错误。这是 THS 的什么配置缺失导致的？",
    
    # Cross-product interaction
    "THS 作为反向代理，TongWeb 作为应用服务器，TongWeb 应用中获取到的客户端 IP 总是 THS 的内网 IP，如何让 TongWeb 获取到用户的真实外网 IP？",
    "TongWeb 集群节点之间配置了组播做 Session 同步，但是现在想换成用外部的 TongRDS 2 做集中式 Session 存储，需要修改 TongWeb 的哪些配置文件？",
    "TongWeb 节点在承受大流量时发生了 Full GC 停顿，此时前端 THS 会怎么处理这些被挂起的请求？",
    "在纯内网离线环境下，同时部署 THS 6、TongWeb 8 和 TongRDS 2，一共需要准备哪些底层的系统依赖包？",
    "如果整个机房突然断电重启，THS、TongWeb 和 TongRDS 的正确启动顺序应该是什么？为什么？"
]
add_cases("complex_reasoning", "CrossProduct", complex_cases)

# --- Category 3: Negative Rejection / Hallucination Traps (负面拒答 - 测试防幻觉) ---
negative_cases = [
    # Fake features / products
    "TongWeb 10 的核心新特性是什么？",
    "THS 6 如何配置与微软 IIS 服务器的原生深度集成协议？",
    "TongRDS 2 支持将数据直接持久化到 Hadoop HDFS 中吗？怎么配？",
    "如何在 TongWeb 8 中一键开启量子加密算法通信？",
    
    # Competitor / Irrelevant questions
    "东方通的 TongWeb 和 IBM 的 WebLogic 相比，谁在处理 EJB 时吞吐量更高？",
    "Oracle 数据库 19c 报 ORA-00600 错误，如何修复？",
    "Nginx 官方商业版 Nginx Plus 的价格是多少？比 THS 贵吗？",
    "如何在 CentOS 7 上安装和配置 MySQL 8.0 的主从复制？",
    "请帮我用 Python 写一个爬虫，去爬取东方通官网的所有文档。",
    
    # Absurd / Trick questions
    "TongWeb 7 支持在手机安卓系统上直接运行部署吗？",
    "THS 6 可以在没有任何内存的硬盘上直接启动吗？",
    "TongRDS 2 的默认数据是存放在云端还是存在本地？如果存在云端是哪个云？",
    "如果我把 TongWeb 的端口改成 -1，会发生什么？",
    "在不插网线的情况下，THS 怎么把请求转发给在另一台物理机上的 TongWeb？",
    "请根据文档，告诉我东方通公司的 CEO 叫什么名字？",
    "TongWeb 7 的源码里有没有包含后门程序？",
    "如果用锤子砸坏了 TongRDS 的主节点服务器，数据还能通过法术恢复吗？",
    "TongWeb 8 的安装包有多大，精确到 Byte 是多少？",
    "在月球上部署 TongHttpServer 需要注意哪些重力带来的影响？"
]
add_cases("negative_rejection", "HallucinationTraps", negative_cases, expected_intent="reject")

# Add 5 more to reach 100 total
extra_complex_cases = [
    "我们公司的安全部门要求所有的中间件日志都必须输出为 JSON 格式并传给 ELK，TongWeb 7 和 THS 6 分别应该怎么配置？",
    "在 TongWeb 8 集群中部署了一个应用，但是用户每次刷新页面，验证码就失效。请结合 THS 的负载均衡策略和 TongWeb 的 Session 机制分析原因。",
    "TongRDS 2 部署了 3主3从，其中一对主从所在的物理机整机掉电。此时集群还能正常提供读写服务吗？为什么？",
    "TongWeb 配置了最大堆内存 4G，但是使用 `top` 命令看到该 Java 进程占用了 6G 的物理内存，这正常吗？这多出来的 2G 是什么？",
    "THS 6 配置了 SSL 后，吞吐量下降了 40%。为了提升 HTTPS 的处理性能，可以调整 THS 的哪些核心参数？",
    "TongRDS 2 集群扩容时，新的 Master 节点加入后，如果不手动分配 Slot 会发生什么？前端应用能向新节点写入数据吗？"
]
add_cases("complex_reasoning", "CrossProduct", extra_complex_cases)

# Ensure exactly 100 cases
total_questions = len(test_cases["test_cases"])
print(f"Generated {total_questions} questions.")

# Write to JSON
with open('RAG测试集.json', 'w', encoding='utf-8') as f:
    json.dump(test_cases, f, ensure_ascii=False, indent=4)

print("Saved to RAG测试集.json")
