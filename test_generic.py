
import asyncio
import websockets
import json

async def test_websocket():
    uri = "ws://localhost:8000/ws/chat"
    query = "请帮我规划一个3台服务器的TongRDS集群"
    
    print(f"Connecting to {uri}...")
    try:
        async with websockets.connect(uri, ping_interval=None) as websocket:
            print("Connected! Sending query...")
            await websocket.send(json.dumps({
                "query": query,
                "thread_id": "ws_test_thread_002",
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
                    elif data.get("type") == "end":
                        print("\n\n[Finished] Connection closed gracefully.")
                        break
                except websockets.exceptions.ConnectionClosed as e:
                    break
    except Exception as e:
        print(f"\n[Exception] {e}")

if __name__ == "__main__":
    asyncio.run(test_websocket())

