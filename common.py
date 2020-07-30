# -*- coding: utf-8 -*-
# @Time : 2020/7/25 12:58
# @Author : Wenlong LI
# @Site :
# @File : common.py
# @Software: PyCharm
from time import time
from functools import  wraps


def print_execute_time(func):
    # 定义嵌套函数，用来打印出装饰的函数的执行时间
    def wrapper(*args, **kwargs):
        # 定义开始时间和结束时间，将func夹在中间执行，取得其返回值
        start = time()
        func_return = func(*args, **kwargs)
        end = time()
        print("---------------------------- * Result * ----------------------------------")
        # 打印方法名称和其执行时间
        print("%s execute result: %s" % (func.__name__, func_return))
        print("%s execute time: %0.2f ms" % (func.__name__, (end - start) * 1000))
        print("--------------------------------------------------------------------------\n")
        # 返回func的返回值
        return func_return

    # 返回嵌套的函数
    return wrapper
