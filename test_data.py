# -*- coding: utf-8 -*-
# @Time : 2020/7/26 12:58
# @Author : Wenlong LI
# @Site :
# @File : test_data.py
# @Software: PyCharm
import random


random_1k = []
for x in range(0, 1*1000):
    random_1k.append(random.randint(0, x))

random_5k = []
for x in range(0, 5*1000):
    random_5k.append(random.randint(0, x))

random_10k = []
for x in range(0, 10*1000):
    random_10k.append(random.randint(0, x))

random_15k = []
for x in range(0, 15*1000):
    random_15k.append(random.randint(0, x))

random_20k = []
for x in range(0, 20*1000):
    random_20k.append(random.randint(0, x))

random_25k = []
for x in range(0, 25*1000):
    random_25k.append(random.randint(0, x))

positive_sort_1k = []
for x in range(0, 1*1000):
    random_10k.append(x)

reverse_sort_1k = []
for x in range(1*1000, 0):
    random_10k.append(x)

