#!/usr/bin/env python
# coding:utf-8

import csv
import os

dirctory = "../files/"
if not os.path.exists(dirctory):
    os.makedirs(dirctory)

csvFile = open("../files/test.csv",'w+')
try:
    writer = csv.writer(csvFile)
    writer.writerow(('number', 'number plus 2', 'number times 2'))
    for i in range(10):
        writer.writerow((i, i + 2, i * 2))
finally:
    csvFile.close()