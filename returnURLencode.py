#! /usr/bin/env python
# _*_ coding: utf-8 _*_

import chardet  # 字符集检测
import urllib

url = "http://www.jd.com"


def automatic_detect( url ):
    content = urllib.urlopen(url).read()
    result = chardet.detect(content)

    encoding = result[ 'encoding' ]

    return encoding


urls = [ 'http://www.baidu.com', 'http://www.163.com', 'http://dangdang.com' ]
for url in urls:
    print url, automatic_detect(url)
