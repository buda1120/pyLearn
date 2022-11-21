# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 15:51:36 2022
爬取搜索引擎的搜索结果
@author: bing
"""
import requests

baiduApi = 'http://www.baidu.com/s'
soApi = 'http://www.so.com/s'

try:
    r1 = requests.get(baiduApi, params={'wd':'Python'})
    print('r1 url:', r1.request.url)
    r1.raise_for_status()
    print(len(r1.text))
except:
    print('Failed')
    
try:
    r2 = requests.get(soApi, params = {'q':'Python'})
    print('r2 url:', r2.request.url)
    r2.raise_for_status()
    print(len(r2.text))
except Exception as e:
    print('Failed r2!')
    print(str(e))
    
    

