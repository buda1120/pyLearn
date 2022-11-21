# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 20:06:46 2022

@author: bing
"""
from xml.etree import ElementTree as ET

tree = ET.parse('data-text.xml')

# 根元素
root = tree.getroot()
data = root.find('Data')

all_data = []

for observation in data:
    record = {}
    for item in observation:
        # item.attrib 返回字典{'Category': xxx, 'Code': xxx}和{'Numeric': xxx}
        lookup_key = list(item.attrib.keys())[0]
        if lookup_key == 'Numeric':
            rec_key = 'NUMERIC'
            rec_value = item.attrib['Numeric']
        else:
            rec_key = item.attrib[lookup_key]
            rec_value = item.attrib['Code']
        
        # print(rec_key, rec_value)
        record[rec_key] = rec_value
        
    all_data.append(record)

for item in all_data:
    print(item)
