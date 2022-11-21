# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 16:57:13 2022

@author: bing
"""
import requests

url = 'http://www.ip168.com/chxip/doGetIp.do'
kv = {'keyword': '36.152.44.95'}
hd = {'User-Agent':'Mozilla/5.0'}
try:
    r = requests.post(url, params=kv, headers=hd)
    r.raise_for_status()
    print(r.text[:1000])
except Exception as e:
    print('Failed!\ninfo:', e)
