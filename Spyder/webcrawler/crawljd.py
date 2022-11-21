# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 15:27:05 2022
爬取京东商品详情页，有爬虫防止措施
@author: bing
"""
import requests

url = 'https://item.jd.com/100016960357.html'
try:
    r1 = requests.get(url)
    print(r1.request.headers)
    print(r1.text[:1000])
    print('---------------------------------')
    # 修改请求头
    kv = {'User-Agent': 'Mozilla/5.0'}
    r = requests.get(url, headers = kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[:1000])
except:
    print('Failed!')