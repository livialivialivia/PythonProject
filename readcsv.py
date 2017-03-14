#! /usr/bin/env python
# _*_ coding: utf-8 _*_


import csv
with open('egg1.csv','rb') as f:
    reader = csv.reader(f)
    for row in reader:
        print row