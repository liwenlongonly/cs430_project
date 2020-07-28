# -*- coding: utf-8 -*-
# @Time : 2020/7/25 12:58
# @Author : Wenlong LI
# @Site :
# @File : median_finding.py
# @Software: PyCharm
import random
from common import print_execute_time
import sys

sys.setrecursionlimit(1000000)


@print_execute_time
def median_finding_randomized(a, p, r, i):
    """
    :param a: input array
    :param p: the left edge of the array, [0...
    :param r: the right edge of the array ...len(array) - 1]
    :param i: i-th smallest number, value range starts from 1
    """
    if a is None or len(a) <= 0:
        return -1
    if p == r:
        return a[p]
    q = _randomized_partition(a, p, r)
    k = q - p + 1
    if i == k:
        return a[q]
    elif i < k:
        return median_finding_randomized(a, p, q - 1, i)
    else:
        return median_finding_randomized(a, q + 1, r, i - k)


@print_execute_time
def median_finding_right(a, p, r, i):
    """
    :param a: input array
    :param p: the left edge of the array, [0...
    :param r: the right edge of the array ...len(array) - 1]
    :param i: i-th smallest number, value range starts from 1
    """
    if a is None or len(a) <= 0:
        return -1
    if p == r:
        return a[p]
    q = _right_partition(a, p, r)
    k = q - p + 1
    if i == k:
        return a[q]
    elif i < k:
        return median_finding_right(a, p, q - 1, i)
    else:
        return median_finding_right(a, q + 1, r, i - k)


def _partition(a, p, r):
    value = a[r]
    i = p - 1
    for j in range(p, r):
        if a[j] <= value:
            i += 1
            a[i], a[j] = a[j], a[i]
        # print("i:%d,j:%d" % (i, j))
        # print(a)
    a[i + 1], a[r] = a[r], a[i + 1]
    return i + 1


def _randomized_partition(a, p, r):
    i = random.randint(p, r)
    # print("random:%d value:%d" %(i, a[i]))
    a[i], a[r] = a[r], a[i]
    return _partition(a, p, r)


def _right_partition(a, p, r):
    i = r
    a[i], a[r] = a[r], a[i]
    return _partition(a, p, r)


if __name__ == '__main__':
    from test_data import *


    def _test(a, median_finding):
        print(a)
        # print(median_finding(a, 0, len(a) - 1, 1))  # min
        print(median_finding(a, 0, len(a) - 1, len(a) // 2))  # median
        # print(median_finding(a, 0, len(a) - 1, len(a)))  # max


    @print_execute_time
    def _median_finding_randomized_test(a, p, r, i):
        return median_finding_randomized(a, p, r, i)


    @print_execute_time
    def _median_finding_right_test(a, p, r, i):
        return median_finding_right(a, p, r, i)


    print("median_finding_randomized >>>>>>>>>>>>>>>")
    testArr1 = positive_sort_1k[:]
    testArr2 = reverse_sort_1k[:]
    testArr3 = random_1k[:]
    _test(testArr1, _median_finding_randomized_test)
    _test(testArr2, _median_finding_randomized_test)
    _test(testArr3, _median_finding_randomized_test)
    print("median_finding_right >>>>>>>>>>>>>>>")
    testArr1 = positive_sort_1k[:]
    testArr2 = reverse_sort_1k[:]
    testArr3 = random_1k[:]
    _test(testArr1, _median_finding_right_test)
    _test(testArr2, _median_finding_right_test)
    _test(testArr3, _median_finding_right_test)
    print("median_finding_randomized >>>>>>>>>>>>>>>")
    testArr4 = random_1k[:]
    testArr5 = random_5k[:]
    testArr6 = random_10k[:]
    testArr7 = random_15k[:]
    testArr8 = random_20k[:]
    testArr9 = random_25k[:]
    _test(testArr4, _median_finding_randomized_test)
    _test(testArr5, _median_finding_randomized_test)
    _test(testArr6, _median_finding_randomized_test)
    _test(testArr7, _median_finding_randomized_test)
    _test(testArr8, _median_finding_randomized_test)
    _test(testArr9, _median_finding_randomized_test)
    print("median_finding_right >>>>>>>>>>>>>>>")
    testArr4 = random_1k[:]
    testArr5 = random_5k[:]
    testArr6 = random_10k[:]
    testArr7 = random_15k[:]
    testArr8 = random_20k[:]
    testArr9 = random_25k[:]
    _test(testArr4, _median_finding_right_test)
    _test(testArr5, _median_finding_right_test)
    _test(testArr6, _median_finding_right_test)
    _test(testArr7, _median_finding_right_test)
    _test(testArr8, _median_finding_right_test)
    _test(testArr9, _median_finding_right_test)
