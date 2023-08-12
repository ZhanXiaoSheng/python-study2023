#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Hello World
author: gxcuizy
date: 2018-10-15
"""

import random

# 程序主入口
if __name__ == '__main__':
    # 打印
    print('Hello World!')

    #获取双色球篮球和红球
    j=0
    red_list=[]
    blue_list = []
    while j<6:
        red_bool = random.randint(1,33)
        if red_bool not in red_list:
            red_list.append(red_bool)
            j+=1
    blue_list.append(random.randint(1,16))
    print('红球为:\n%s'%red_list)
    print('篮球为:\n%s'%blue_list)


    # 取4个随机数
    i = 0
    rand_list = []
    while i < 4:
        rand_num = random.randint(0, 499)
        if rand_num not in rand_list:
            rand_list.append(rand_num)
            i += 1
    # 输出组队随机编码
    print(rand_list)
