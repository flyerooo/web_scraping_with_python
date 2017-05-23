#!/usr/bin/env python
# coding:utf-8

#!/usr/bin/env python
# coding=utf-8
from urllib.request import Request,urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
import re
import csv
import os


def getHTML(i):
    url = 'http://www.jianshu.com/trending/weekly?page={}'.format(i)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'}
    try:
        request = Request(url=url, headers=headers)
        html = urlopen(request)
        bsObj = BeautifulSoup(html.read(), 'lxml')
        items = bsObj.findAll("div", {"class": "content"})
    except HTTPError as e:
        print(e)
        exit()
    return items

def getArticleInfo(items):
    articleInfo= []
    for item in items:
        author = item.find("a", {"class": "blue-link"}).get_text()
        title = item.find("a", {"class": "title"}).get_text()
        other = item.find("div", {"class": "meta"}).get_text()
        pattern = re.compile('(\d+)')
        content = re.findall(pattern, other)
        view = content[0]
        comment = content[1]
        like = content[2]
        money = content[3] if (len(content) == 4) else "zero"  # 不太严谨，暂时这么做
        articleInfo.append([author, title, view, comment, like, money])
    return articleInfo

dir = "../jianshu/"
if not os.path.exists(dir):
    os.makedirs(dir)
csvFile = open("../jianshu/jianshuSevenDaysArticles.csv","wt",encoding='utf-8')
writer = csv.writer(csvFile)
writer.writerow(("author", "title", "view", "comment", "like", "money"))
try:
    for i in range(1, 6):
        items = getHTML(i)
        articleInfo = getArticleInfo(items)
        for item in articleInfo:
                writer.writerow(item)

finally:
    csvFile.close()


