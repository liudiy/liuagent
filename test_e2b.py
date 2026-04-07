import os
from dotenv import load_dotenv
load_dotenv()
from e2b_code_interpreter import Sandbox

print('Testing E2B Sandbox connection...')
try:
    sbx = Sandbox(api_key=os.environ.get("E2B_API_KEY"))
    print('Connected successfully! Sandbox ID:', getattr(sbx, 'id', 'unknown'))
    execution = sbx.run_code('print("Hello from E2B!")')
    print('Execution output:', execution.logs.stdout)
    sbx.close()
except Exception as e:
    print('Error connecting to Sandbox:', e)
