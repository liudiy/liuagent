import random
import datetime
import os

os.makedirs('data', exist_ok=True)
log_files = ['data/prod_api_v2.log', 'data/payment_gateway_2023.txt']

for lf in log_files:
    with open(lf, 'w') as f:
        base_time = datetime.datetime.now()
        for i in range(50):
            current_time = base_time + datetime.timedelta(minutes=i)
            response_time = random.randint(20, 300)
            if i % 10 == 0:
                response_time += 1500 # 模拟偶尔的卡顿
            f.write(f"{current_time.strftime('%Y-%m-%d %H:%M:%S')} [INFO] Request processed in {response_time}ms\n")
    print(f"Generated {lf}")
