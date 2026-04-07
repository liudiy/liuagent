import random
import datetime
import os

os.makedirs('data', exist_ok=True)
with open('data/test_server.log', 'w') as f:
    base_time = datetime.datetime.now()
    for i in range(100):
        current_time = base_time + datetime.timedelta(minutes=i)
        response_time = random.randint(50, 500)
        if i % 15 == 0:
            response_time += random.randint(1000, 3000) # 模拟卡顿
            level = 'ERROR'
        elif i % 5 == 0:
            level = 'WARN'
        else:
            level = 'INFO'
        f.write(f"{current_time.strftime('%Y-%m-%d %H:%M:%S')} [{level}] [Thread-{i%10}] Request /api/data processed in {response_time}ms\n")
print('Test log created at data/test_server.log')
