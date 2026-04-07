import requests
import json
import time

def test_pydantic_reflection():
    url = "http://localhost:8000/chat/stream"
    # 发送一个会报错的工具调用请求
    params = {
        "query": "用 python 执行 print(1/0)",
        "thread_id": "test_pydantic_123",
        "user_id": "test_user"
    }
    
    try:
        print("开始发送请求...")
        response = requests.get(url, params=params, stream=True)
        response.raise_for_status()
        
        reflection_data = None
        
        for line in response.iter_lines():
            if line:
                decoded_line = line.decode('utf-8')
                print(decoded_line)
                if decoded_line.startswith('data: '):
                    data_str = decoded_line[6:]
                    try:
                        data = json.loads(data_str)
                        if data.get("type") == "reflection_log":
                            reflection_data = data
                            print("\n=== 成功捕获 Reflection Log ===")
                            print(json.dumps(data, indent=2, ensure_ascii=False))
                    except json.JSONDecodeError:
                        pass
                        
        if reflection_data:
            print("\n测试通过: 成功解析并输出了包含 Pydantic 约束的 Reflection 数据。")
        else:
            print("\n测试失败: 未找到 Reflection 日志，或者后端格式有误。")
            
    except requests.exceptions.RequestException as e:
        print(f"请求失败: {e}")

if __name__ == "__main__":
    test_pydantic_reflection()
