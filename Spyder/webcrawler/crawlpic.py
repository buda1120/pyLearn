# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 16:18:37 2022
爬取图片
@author: bing
"""
import requests
import os

url = 'https://preview.qiantucdn.com/auto_machine/20201119/109c9ac0-47f1-47b3-8724-b7543c272f0b.png!w1024_new_small'
# url = 'https://bing.com/th?id=OHR.HainesEagle_ZH-CN1542376030_UHD.jpg'
path = os.getcwd() + os.sep + 'abc.jpg'

try:
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path, 'wb') as f:
            f.write(r.content)
            print('文件保存成功')
    else:
        print('文件已存在:', path)
except Exception as e:
    print('Failed!\ninfo:', e)
            

