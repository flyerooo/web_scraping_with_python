#!/usr/bin/env python
# coding:utf-8

import requests
# 提交表单信息
params = {'first': 'Ryan', 'lastname': 'Mitchell'}
r = requests.post("http://pythonscraping.com/pages/files/processing.php", data=params)
print(r.text)