import requests
import json
import urllib.parse
import os
import glob

# 清理之前的输出
for f in glob.glob('output/*.png'):
    os.remove(f)

queries = [
    # 测试1：明确给出不常规的文件名
    ("分析一下 prod_api_v2.log 文件，提取它的响应时间并画一个折线图。记得告诉我图表保存在哪了。", "dyn-test-1"),
    
    # 测试2：完全不给文件名，让它自己去找
    ("我刚才上传了一个叫做 payment 相关的文本日志文件，我不记得全名了。帮我找找它，提取里面的响应时间并画个折线图。", "dyn-test-2"),
]

for q, tid in queries:
    print(f"\n==============================================")
    print(f"Testing Query: {q}")
    print(f"==============================================")
    
    url = f"http://localhost:8000/chat/stream?query={urllib.parse.quote(q)}&thread_id={tid}&user_id=test"
    
    try:
        response = requests.get(url, stream=True)
        for line in response.iter_lines():
            if line:
                try:
                    event_data = line.decode('utf-8')
                    if event_data.startswith('data: '):
                        data_json = json.loads(event_data[6:])
                        if data_json.get('type') == 'token':
                            print(data_json['content'], end='', flush=True)
                        elif data_json.get('type') == 'tool_end':
                            print('\n\n--- [工具执行完毕] ---')
                            print(data_json.get('output', '')[:300] + '...')
                            print('-----------------------\n')
                except Exception:
                    pass
    except Exception as e:
        print("请求错误:", e)
        
    print("\n\n--- 检查 Output 文件夹 ---")
    pngs = glob.glob('output/*.png')
    print("当前生成的图片:", pngs)
    print("\n")
