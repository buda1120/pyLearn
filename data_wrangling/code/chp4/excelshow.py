# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 21:04:48 2022

@author: bing
"""
# =============================================================================
# xlrd
# xlwt
# xlutils
# =============================================================================
import xlrd


book = xlrd.open_workbook('SOWC 2014 Stat Tables_Table 9.xls')
# for sheet in book.sheets():
#     print(sheet.name)
sheet = book.sheet_by_name('Table 9 ')
print(sheet)