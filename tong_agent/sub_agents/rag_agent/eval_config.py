import os
# 用来加载 .env 文件里的 API KEY
from dotenv import load_dotenv
# DeepEval 规定自定义模型必须继承这个基类
from deepeval.models.base_model import DeepEvalBaseLLM
# 因为阿里云 Qwen 兼容 OpenAI 接口，我们偷懒用这个现成的客户端
from langchain_openai import ChatOpenAI

# 别忘了先加载环境变量，否则后面读不到 KEY
load_dotenv()

class QwenEvalLLM(DeepEvalBaseLLM):
    def __init__(self):
        self.model_name = "qwen-plus"
        
        # 2. 从环境变量拿 Key，拿不到就报错提醒自己
        api_key = os.environ.get("DASHSCOPE_API_KEY")
        if not api_key:
            raise ValueError("❌ 找不到 DASHSCOPE_API_KEY，请检查 .env 文件！")
            
        self.llm = ChatOpenAI(
            model=self.model_name,
            openai_api_key=api_key,
            openai_api_base="https://dashscope.aliyuncs.com/compatible-mode/v1",
            temperature=0,  # 评估时我们要它严谨，不要随机乱编，所以设为 0
        )

    # DeepEval 会调用这个方法加载模型
    def load_model(self):
        return self.llm

    # DeepEval 会调用这个方法生成评估结果（同步版）
    # 比如它问：“这句话有幻觉吗？”，模型回答：“没有。”
    def generate(self, prompt: str) -> str:
        # invoke 是 LangChain 的标准调用方法
        return self.llm.invoke(prompt).content

    # DeepEval 会调用这个方法生成评估结果（异步版，跑得快）
    async def a_generate(self, prompt: str) -> str:
        # ainvoke 是异步调用
        result = await self.llm.ainvoke(prompt)
        return result.content

    # DeepEval 只是想知道你用的啥模型
    def get_model_name(self):
        return self.model_name


def generate_manual_testset():
    """
    手动定义一些 Golden Test Cases (黄金测试集)。
    包含：Query (问题) 和 Expected Output (标准答案，可选)。
    """
    test_cases = [
        {
            "input": "TongWeb 的负载均衡支持哪些算法？",
            "expected_output": "TongWeb 负载均衡支持以下算法：轮询 (默认)、随机 (random)、IP 哈希 (ip_hash)、Hash 策略 (如 url_hash)、最小连接数 (least_conn) 和 Sticky Cookie 会话保持。"
        },
        {
            "input": "如何配置 TongWeb 的最大线程数？",
            "expected_output": "可以在 tongweb.xml 配置文件中，修改 <thread-pool> 元素的 max-threads 属性来配置最大线程数。"
        },
        {
            "input": "TongWeb 启动失败报错 'Address already in use' 怎么办？",
            "expected_output": "这通常意味着端口被占用。可以使用 netstat -anp | grep <端口号> 查找占用进程并 kill 掉，或者在 tongweb.xml 中修改 TongWeb 的监听端口。"
        }
    ]
    return test_cases





if __name__ == "__main__":
    # 测试一下 Qwen 是否能连通
    try:
        qwen = QwenEvalLLM()
        print("正在测试 Qwen 连接...")
        response = qwen.generate("你好，DeepEval！")
        print(f"✅ 连接成功，回复：{response}")
    except Exception as e:
        print(f"❌ 连接失败：{e}")