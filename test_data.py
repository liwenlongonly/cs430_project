# -*- coding: utf-8 -*-
# @Time : 2020/7/26 12:58
# @Author : Wenlong LI
# @Site :
# @File : test_data.py
# @Software: PyCharm
import random


def create_random_array(array, max_value):
    for x in range(0, max_value):
        array.append(random.randint(0, max_value))


random_1k = []
create_random_array(random_1k, 1*1000)

random_5k = []
create_random_array(random_5k, 5*1000)

random_10k = []
create_random_array(random_10k, 10*1000)

random_15k = []
create_random_array(random_15k, 15*1000)

random_20k = []
create_random_array(random_20k, 20*1000)

random_25k = []
create_random_array(random_25k, 25*1000)

positive_sort_1k = []
for x in range(0, 1*1000):
    positive_sort_1k.append(x+1)

reverse_sort_1k = []
for x in range(0, 1*1000):
    reverse_sort_1k.append(1*1000-x)
