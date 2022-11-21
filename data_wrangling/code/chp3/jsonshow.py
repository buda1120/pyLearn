# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 19:56:12 2022

@author: bing
"""
import json

json_data = open('data-text.json').read()

data = json.loads(json_data)

for item in data:
    print(item)