#! /usr/bin/env python
# _*_ coding: utf-8 _*_

# 将文件夹下所有图片名称加上'_livia'

import re
import os
import time

def change_imagename(path):
    global i
    # 检查给出的路径是否是一个目录,是否是一个文件
    if not os.path.isdir(path) and not os.path.isfile(path):
        return False
    # 如果给出的路径是一个文件
    if os.path.isfile(path):
        # 返回一个路径的目录名和文件名,这里若是/test/old/one.jpg,就是返回file_path=('/test/old','one.jpg')
        file_path = os.path.split(path)
        # file_path[1]得到的结果就是('one.jpg'),这里以'.'分隔,得到lists=(one,jpg)
        lists = file_path[1].split('.')
        # list[-1]取得最后一个元素,这里为file_ext=jpg
        file_ext = lists[-1]
        img_ext = ['bmp','jpeg','gif','psd','png','jpg']
        # 如果这些文件是以img_ext结尾命名的,就重命名
        if file_ext in img_ext:
            os.rename(path,file_path[0]+'/'+lists[0]+'_livia.'+file_ext)
            # 按照上面的逻辑,file_path[0]=('/test/old'),lists[0]=one,结果为:/test/old/one_livia.jpg,就是将/test/old/one.jpg重命名为:/test/old/one_livia.jpg
            i+=1
    # 如果给出的路径是一个目录
    elif os.path.isdir(path):
        # listdir()返回指定目录下的所有文件和目录名
        for x in os.listdir(path):
            # 返回文件名,再次call change_imagename,进行文件重命名
            change_imagename(os.path.join(path,x))

img_dir = '/Users/interviewer/Documents/pic for test/Old'
img_dir = img_dir.replace('\\','/')  #将目录的/都更换为\\
start = time.time()
i = 0
change_imagename(img_dir)
c = time.time() - start
print('程序运行耗时:%0.2f'%(c))
print('总共处理了 %s 张图片'%(i))