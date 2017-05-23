#!/usr/bin/env python
# coding:utf-8

import requests
# 登录后获取cookie，然后将cookie用于请求中
params = {'firstname': 'Ryan', 'lastname': 'Mitchell'}
r = requests.post("http://pythonscraping.com/pages/files/processing.php", data=params)
print("Cookie is set to: ")
print(r.cookies.get_dict())
print("---------------")
print("Going to profile page...")
r = requests.get("http://pythonscraping.com/pages/cookies/profile.php", cookies=r.cookies)
print(r.text)
