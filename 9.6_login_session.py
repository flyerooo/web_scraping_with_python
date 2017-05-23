#!/usr/bin/env python
# coding:utf-8

import requests

session = requests.Session()

params = {'username': 'username', 'password': 'password'}
s = requests.post("http://pythonscraping.com/pages/files/processing.php", data=params)
print("Cookie is set to: ")
print(s.cookies.get_dict())
print("------------")
print("Going to profile page...")
s = session.get("http://pythonscraping.com/pages/cookies/profile.php")
print(s.text)