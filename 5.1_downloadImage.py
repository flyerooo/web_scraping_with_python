#!/usr/bin/env python
# coding:utf-8

import os
from urllib.error import HTTPError
from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup

downloadDirectory = "download"
baseUrl = "http://pythonscraping.com"

# 对URL进行清理和标准化，去掉外链
def getAbsoluteURL(baseUrl, source):
    if source.startswith("http://wwww."):
        url = "http://" + source[11:]
    elif source.startswith("http://"):
        url = source
    elif source.startswith("www."):
        url = source[4:]
        url = "http://" + url
    else:
        url = baseUrl + "/" + source
    if baseUrl not in url:
        return url

# 获得文件的绝对路径
def getDownloadPath(baseUrl, absoluteUrl, downloadDirectory):
    path = absoluteUrl.replace("www.", "")
    path = path.replace(baseUrl, "")
    path = downloadDirectory + path
    directory = os.path.dirname(path)

    if not os.path.exists(directory):
        os.makedirs(directory)
    return path

def getDownloadList():
    try:
        html = urlopen("http://www.pythonscraping.com")
        bsObj = BeautifulSoup(html, "lxml")
        downloadList = bsObj.findAll(src=True)
    except HTTPError as e:
        print(e)
    return downloadList

downloadList = getDownloadList()
for download in downloadList:
    fileUrl = getAbsoluteURL(baseUrl, download["src"])
    if fileUrl is not None:
        print(fileUrl)

        urlretrieve(fileUrl, getDownloadPath(baseUrl, fileUrl, downloadDirectory))
