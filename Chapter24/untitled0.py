#!/usr/bin/env python

# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 13:44:08 2016

@author: zoumucheng
"""

#!/usr/bin/python
# -*- coding: UTF-8 -*-

try:
    fh = open("testfile", "w")
    fh.write("这是一个测试文件，用于测试异常!!")
except IOError:
    print ("Error: 没有找到文件或读取文件失败")
else:
    print ("内容写入文件成功")
    fh.close()