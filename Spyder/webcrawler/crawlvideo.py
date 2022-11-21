# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 16:46:08 2022
爬取视频: web网页 F12--Network--Media--request url
@author: bing
"""
import requests
import os

url = 'https://701-18.vod.tv.itc.cn/sohu/v1/TmwUqEItfDcRh2NAoMd7z8W7qT060TWbu8dGypCHqM14wmfcymcAr.mp4?k=GCIi7w&p=XZhuOp33OUoWXZxIypfS0p0cWhoGNh2sY&r=TmI20LscWOo3NMAcWYdAqhNAhE6ObtcL0YvFM2bIlwGHUGLtUgFs3hBcLYFhRkIWhoCNLfcWB1svmXAyBj&q=OpCAhW7IRYodRD6twmfCyY2sWhyHfheslG6sWGXOWho2ZDvtRY14WDb4wm4cWJvXvmscWY&nid=701'
path = os.getcwd() + os.sep + 'vd.mp4'

try: 
    if not os.path.exists(path):
        r = requests.get(url)
        r.raise_for_status()
        with open(path, 'wb') as f:
            f.write(r.content)
            print('下载成功')
    else:
        print('目录已存在')
except Exception as e:
    print('Failed!\ninfo:', str(e))

