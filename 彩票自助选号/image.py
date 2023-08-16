#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   image.py
@Time    :   2023/08/15 13:38:34
@Author  :   zhangsheng 
@Version :   1.0
@Desc    :   处理图片
'''

# here put the import lib

# base64转码，将转码后的文件存入icon.py中
open_icon = open("ball.ico", "rb")
b64str = base64.b64encode(open_icon.read())
open_icon.close()
write_data = "img = %s" % b64str
f = open("icon.py", "w+")
f.write(write_data)
f.close()