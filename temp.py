#!/usr/bin/env python
# coding:utf-8

from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import json
import datetime
import random
import re

html = urlopen("http://www.pythonscraping.com")
bsObj = BeautifulSoup(html, "lxml")
downloadList = bsObj.findAll(src=True)

baseUrl = "http://pythonscraping.com"

def getAbsoluteURL(baseUrl, source):
    if source.startswith("http://www."):
        url = "http://" + source[11:]
    else:
        url = baseUrl + "/" + source
    if baseUrl not in url:
        return None
    return url
for download in downloadList:
    fileUrl = getAbsoluteURL(baseUrl, download["src"])
    print(fileUrl)
