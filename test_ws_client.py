import asyncio
import websockets
import json

async def test_websocket():
    uri = "ws://localhost:8000/ws/chat"
    query = "我有8台服务器，10.10.22.100-10.10.22.107，我该如何使用这些机器。安装TongHttpServer，Tongweb，TongRDS。每个产品，都需要支持集群。机器配置如下：10.10.22.100，CPU x86_64 32核，内存16G，硬盘500G,10.10.22.101，CPU x86_64 32核，内存16G，硬盘500G,10.10.22.102，CPU x86_64 16核，内存64G，硬盘500G,10.10.22.103，CPU x86_64 16核，内存64G，硬盘500G,10.10.22.104，CPU x86_64 16核，内存32G，硬盘500G,10.10.22.105，CPU x86_64 16核，内存32G，硬盘500G,10.10.22.106，CPU x86_64 32核，内存32G，硬盘500G,10.10.22.107，CPU x86_64 32核，内存32G，硬盘500G"
    
    print(f"Connecting to {uri}...")
    try:
        async with websockets.connect(uri, ping_interval=None) as websocket:
            print("Connected! Sending query...")
            await websocket.send(json.dumps({
                "query": query,
                "thread_id": "ws_test_thread_001",
                "user_id": "test_user"
            }))
            
            full_response = ""
            while True:
                try:
                    response = await websocket.recv()
                    data = json.loads(response)
                    
                    if data.get("type") == "token":
                        content = data.get("content", "")
                        full_response += content
                        print(content, end="", flush=True)
                    elif data.get("type") == "tool_start":
                        print(f"\n[Tool Start] {data.get('tool')}")
                    elif data.get("type") == "error":
                        print(f"\n[ERROR] {data.get('message')}")
                        break
                    elif data.get("type") == "end":
                        print("\n\n[Finished] Connection closed gracefully.")
                        break
                    else:
                        print(f"\n[Other Event] {data.get('type')} - {str(data)[:100]}")
                except websockets.exceptions.ConnectionClosed as e:
                    print(f"\n[Connection Closed] {e}")
                    break
    except Exception as e:
        print(f"\n[Exception] {e}")

if __name__ == "__main__":
    asyncio.run(test_websocket())