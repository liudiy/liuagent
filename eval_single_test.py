import os
import json
import asyncio
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.environ.get("DASHSCOPE_API_KEY", "")
os.environ["OPENAI_BASE_URL"] = "https://dashscope.aliyuncs.com/compatible-mode/v1"

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field

class EvalResult(BaseModel):
    score: float = Field(description="评分，范围 0.0 到 1.0")
    reason: str = Field(description="给出该评分的详细原因和分析")

judge_llm = ChatOpenAI(model="qwen-turbo", temperature=0).with_structured_output(EvalResult)

relevancy_prompt = PromptTemplate.from_template("""
你是一个严谨的评估专家。请评估给定的【回答】是否准确且相关地解答了【用户问题】，并且是否包含了【参考答案】中的核心要求。

【要求】:
1. 【参考答案】中的核心要求是必须满足的。
2. 如果【回答】不仅包含了【参考答案】的核心要求，还提供了额外有用的、结构化的架构分析，这是加分项。
3. 如果【回答】准确、完整地解答了【用户问题】并覆盖了【参考答案】，给出 score = 1.0。
4. 如果【回答】部分覆盖，给出 score = 0.5。
5. 如果【回答】完全偏离，给出 score = 0.0。

【用户问题】:
{question}

【参考答案】:
{ground_truth}

【待评估的回答】:
{answer}

请提供 score 和 reason。
""")

async def evaluate():
    question = "一个环境，安装了TongHttpServer，Tongweb，TongRDS，部署在8个不同的服务器上，如何保证全链路数据安全？"
    ground_truth = "将TongHttpServer，Tongweb，TongRDS，每一个实例，都配置为支持SSL，即可保证全链路数据安全。需要列出具体的，每个产品，配置SSL的方法"
    agent_answer = """为保证部署在8台服务器上的TongHttpServer、Tongweb、TongRDS环境实现全链路数据安全，现提供以下架构规划与安全实施方案。 
 
 一、 服务器资源分配与高可用拓扑规划 
 首先，基于生产环境隔离原则和高可用要求，对8台服务器进行规划： 
 
 服务器编号 	 部署组件 	 角色说明 	 高可用考虑 
 S1, S2 	 TongHttpServer 	 负载均衡层（Active-Standby 或 集群） 	 实现流量入口高可用，避免单点故障。 
 S3, S4 	 Tongweb 	 应用服务器集群节点1、节点2 	 实现应用层无状态水平扩展和高可用。 
 S5, S6, S7 	 TongRDS 	 数据库集群节点（如：一主两从，或三节点对等集群） 	 满足数据库法定票数(Quorum)，确保数据一致性与高可用。 
 S8 	 安全管理/监控节点 	 部署统一日志审计、安全监控平台、证书管理服务等。 	 集中安全管控，不承载业务流量。 
 设计依据：此规划严格遵守“一机一用”隔离原则，将网络I/O密集型（TongHttpServer）、应用计算密集型（Tongweb）、数据存储密集型（TongRDS）分离，并满足了各组件最小高可用节点数要求。剩余一台服务器专用于安全管理，符合安全运营最佳实践。 
 
 二、 全链路数据安全防护策略与具体措施 
 以下策略覆盖数据从客户端到数据库存储的完整路径。 
 
 1. 网络与传输层安全 (Client → TongHttpServer → Tongweb) 
 
 入口加密 (TongHttpServer)： 
 强制HTTPS：在TongHttpServer上配置SSL/TLS，禁用低版本协议（如SSLv2/v3），仅启用TLSv1.2和TLSv1.3。 
 使用强密码套件：配置ssl_ciphers，优先使用前向保密(FS)的密码套件。 
 证书管理：使用可信CA签发的服务器证书，并配置ssl_certificate和ssl_certificate_key路径。定期轮换证书。 
 内部通信加密： 
 TongHttpServer 到 Tongweb：配置TongHttpServer的upstream模块，使用https协议与后端Tongweb通信（需在Tongweb端同样启用HTTPS），或部署在安全的内部VLAN/专网中。 
 会话安全：若启用会话保持，在TongHttpServer配置中使用sticky_secure指令对Cookie进行盐值混淆，防止会话劫持。 
 2. 应用层安全 (Tongweb) 
 
 应用安全加固： 
 安全头：在Tongweb或通过TongHttpServer配置HTTP安全响应头，如Content-Security-Policy, X-Frame-Options, X-Content-Type-Options, Strict-Transport-Security等。 
 输入验证与输出编码：在业务应用中实施，防止SQL注入、XSS等漏洞。 
 API安全：利用Tongweb的REST API配置功能（如urlPatterns），对敏感接口实施细粒度访问控制。 
 数据库连接安全 (Tongweb → TongRDS)： 
 加密连接：在Tongweb的JDBC安全域配置中，确保jdbcURL使用加密协议（如JDBC over SSL/TLS）。 
 凭据保护：使用digestAlgorithm（如SM3、SHA-256）对配置中的jdbcPassword进行加密存储，避免明文密码。 
 最小权限：配置的数据库用户（jdbcUser）仅拥有应用所需的最小权限。 
 3. 数据存储层安全 (TongRDS) 
 
 静态数据加密： 
 透明数据加密(TDE)：在TongRDS中启用数据库存储加密，对数据文件、备份文件进行加密。 
 字段级加密：对极端敏感数据（如身份证号、银行卡号），在应用层进行加密后再存储。 
 访问控制与审计： 
 网络白名单：在TongRDS配置中，严格限制访问源IP，仅允许Tongweb应用服务器（S3, S4）和管理节点（S8）访问。 
 数据库审计：启用TongRDS的完整SQL审计日志，记录所有数据访问行为，日志集中发送至S8的审计平台。 
 4. 安全管理与运营 
 
 集中监控与审计 (S8)： 
 部署SIEM或日志审计平台，集中收集TongHttpServer访问日志、Tongweb应用日志、TongRDS审计日志，进行关联分析和异常告警。 
 部署漏洞扫描和配置合规检查工具，定期对三层面组件进行安全检查。 
 持续安全实践： 
 最小权限原则：操作系统、中间件、数据库账户均按需分配权限。 
 补丁与更新：建立流程，定期更新所有组件的安全补丁。 
 备份与恢复：对TongRDS数据及关键配置文件进行加密备份，定期测试恢复流程。 
 渗透测试：定期对全链路进行渗透测试和安全评估。 
 三、 关键配置点示例（基于检索知识） 
 TongHttpServer (SSL配置示例): 
 server { 
     listen 443 ssl; 
     ssl_certificate /path/to/server.crt; 
     ssl_certificate_key /path/to/server.key; 
     ssl_protocols TLSv1.2 TLSv1.3; 
     ssl_ciphers HIGH:!aNULL:!MD5; 
     # ... 其他配置 ... 
 } 
 Tongweb (JDBC安全域配置思路): 在Tongweb控制台或配置文件中，配置数据源时，启用密码加密，并确保连接串带加密选项。 
 总结：本方案通过合理的资源隔离与高可用拓扑奠定了安全基础，并实施了覆盖网络传输加密、应用防护、数据存储加密、统一安全管控的纵深防御体系，可有效保障全链路数据在传输、处理和存储过程中的机密性、完整性和可用性。"""

    print("⚖️ 正在让 Qwen 裁判评估 Agent 的回答与标准答案的区别...")
    result = await judge_llm.ainvoke(relevancy_prompt.format(
        question=question, 
        ground_truth=ground_truth, 
        answer=agent_answer
    ))
    print(f"\n📊 评分: {result.score}")
    print(f"📝 裁判分析:\n{result.reason}")

if __name__ == "__main__":
    asyncio.run(evaluate())