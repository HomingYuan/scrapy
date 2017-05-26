#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Homing
@software: PyCharm Community Edition
@file: doubanmm.py
@time: 2017/5/26 22:01
"""
import urllib.request
from bs4 import BeautifulSoup


def crawl(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
    req = urllib.request.Request(url, headers=headers)
    page = urllib.request.urlopen(req, timeout=40)
    contents = page.read()
    soup = BeautifulSoup(contents, 'lxml')  # 加一个解析器
    my_girl = soup.find_all('img')
    i = 0
    for girl in my_girl:
        i += 1
        print("第%d张照片"%i)
        link = girl.get('src')
        print(link)
        content2 = urllib.request.urlopen(link).read()
        with open(u'D:\Big_data\pic' + '/' + link[-11:], 'wb') as code:
            code.write(content2)


page_start = 500
page_stop = 4944
for page in range(page_start, page_stop, 1):
    page += 1
    url = 'http://www.dbmeinv.com/?pager_offset=%s' % page
    crawl(url)

print("玩蛇python之家提示, MM图片下载完毕。！")










