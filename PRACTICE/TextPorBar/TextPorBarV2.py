#TextPorBarV2.py
#单行动态刷新
import time

for i in range(101):
    print("\r{:3}%".format(i), end="")
    time.sleep(0.2)
#使用命令行运行 python xx.py
