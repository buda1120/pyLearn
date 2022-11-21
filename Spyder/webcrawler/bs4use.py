# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 17:34:05 2022
BeautifulSoup库的使用
@author: bing
"""
import requests
from bs4 import BeautifulSoup

try:
    r = requests.get('http://python123.io/ws/demo.html')
    r.raise_for_status()
    demo = r.text
    soup = BeautifulSoup(demo, 'html.parser')
    print(soup.prettify())
except Exception as e:
    print('Failed!\n', str(e))
