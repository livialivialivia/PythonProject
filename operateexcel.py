#! /usr/bin/env python
# _*_ coding: utf-8 _*_

import xlrd
workbook = xlrd.open_workbook('demo.xlsx')  #打开exce数据表
SheetList = workbook.sheet_names()  # 读取电子表到列表
SheetName = SheetList[0]    # 读取第一个电子表的名称
Sheet1 = workbook.sheet_by_index(0)     # 电子表索引从0开始
Sheet2 = workbook.sheet_by_name(SheetName)  # 实例化电子表对象

m=0
f=0
for i in range(Sheet1.nrows):
    rows = Sheet1.row_values(i)
    if rows[2]=='male':
        m+=1
    elif rows[2]=='female':
        f+=1
print "Male: %s" %m
print "Female: %s " %f