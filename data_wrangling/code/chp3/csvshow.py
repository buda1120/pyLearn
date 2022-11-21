# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 19:36:32 2022

@author: bing
"""
import csv

csvfile = open('data-text.csv', 'rt')
# reader = csv.reader(csvfile)
reader = csv.DictReader(csvfile)

for row in reader:
    print(row)
    
csvfile.close()