#!/usr/bin/env python
# coding:utf-8

import pymysql

conn = pymysql.connect(host='127.0.0.1',
                       user='root',
                       password='jeff',
                       db='mysql',
                       )

cur = conn.cursor()
cur.execute("USE scraping")
cur.execute("SELECT * FROM pages WHERE id=1")
print(cur.fetchone())
cur.close()
conn.close()