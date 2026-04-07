
import asyncio
from langchain_core.runnables import RunnableLambda
from langchain_core.callbacks import BaseCallbackHandler

class NameCheckHandler(BaseCallbackHandler):
    def on_chain_start(self, serialized, inputs, *, run_id, parent_run_id=None, **kwargs):
        # LangChain often puts the name in serialized['name'] OR we can rely on run object attributes if we had access
        # But here we check serialized
        name = serialized.get("name") if serialized else "Unknown"
        print(f"[START] Name: '{name}'")

def my_func(x):
    return x

async def main():
    handler = NameCheckHandler()
    
    print("Testing RunnableLambda with name param...")
    runnable = RunnableLambda(my_func, name="MyExplicitName")
    await runnable.ainvoke("hi", config={"callbacks": [handler]})

if __name__ == "__main__":
    asyncio.run(main())
