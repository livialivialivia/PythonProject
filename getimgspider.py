#! /usr/bin/env python
# _*_ coding: utf-8 _*_

import urllib
import re

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getImg(html):
    reg = r'src="(.+?\.jpg)"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    for imgurl in imglist:
        x = 100
        urllib.urlretrieve(imgurl,"%s.jpg" %x)
        x+=1
    return imglist

html = getHtml("https://tieba.baidu.com/p/2460150866?red_tag=3569129009")
print getImg(html)
print 'spider downlod success!!'


# IOError: [Errno ftp error] [Errno 60] Operation timed out
# 只下载了100.jpg图片