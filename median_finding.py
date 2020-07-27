# -*- coding: utf-8 -*-
# @Time : 2020/7/25 12:58
# @Author : Wenlong LI
# @Site :
# @File : median_finding.py
# @Software: PyCharm
import random
from common import print_execute_time


@print_execute_time
def median_finding_randomized(a, p, r, i):
    """
    :param a: input array
    :param p: the left edge of the array, [0...
    :param r: the right edge of the array ...len(array) - 1]
    :param i: i-th smallest number, value range starts from 1
    """
    return _median_finding_randomized(a, p, r, i)


@print_execute_time
def median_finding_sort(a, p, r, i):
    """
    :param a: input array
    :param p: the left edge of the array, [0...
    :param r: the right edge of the array ...len(array) - 1]
    :param i: i-th smallest number, value range starts from 1
    """
    if a is None or len(a) <= 0:
        return -1
    result = _merge_sort(a)
    return result[i-1]


def _partition(a, p, r):
    value = a[r]
    i = p - 1
    for j in range(p, r):
        if a[j] <= value:
            i += 1
            a[i], a[j] = a[j], a[i]
        # print("i:%d,j:%d" % (i, j))
        # print(a)
    a[i+1], a[r] = a[r], a[i+1]
    return i+1


def _randomized_partition(a, p, r):
    i = random.randint(p, r)
    # print("random:%d value:%d" %(i, a[i]))
    a[i], a[r] = a[r], a[i]
    return _partition(a, p, r)


def _median_finding_randomized(a, p, r, i):
    if a is None or len(a) <= 0:
        return -1
    if p == r:
        return a[p]
    q = _randomized_partition(a, p, r)
    k = q - p + 1
    if i == k:
        return a[q]
    elif i < k:
        return _median_finding_randomized(a, p, q - 1, i)
    else:
        return _median_finding_randomized(a, q + 1, r, i - k)


def _merge_sort(a):
    n = len(a)
    if n <= 1:
        return a
    mid = n // 2

    left_li = _merge_sort(a[:mid])
    right_li = _merge_sort(a[mid:])

    left_pointer = 0
    right_pointer = 0
    result = []

    while left_pointer < len(left_li) and right_pointer < len(right_li):
        if left_li[left_pointer] <= right_li[right_pointer]:
            result.append(left_li[left_pointer])
            left_pointer += 1
        else:
            result.append(right_li[right_pointer])
            right_pointer += 1
    result += left_li[left_pointer:]
    result += right_li[right_pointer:]
    return result


def _test(a, median_finding):
    print(a)
    # print(median_finding(a, 0, len(a) - 1, 1))  # min
    print(median_finding(a, 0, len(a) - 1, len(a)//2))  # median
    # print(median_finding(a, 0, len(a) - 1, len(a)))  # max


if __name__ == '__main__':
    from test_data import *
    testArr1 = positive_sort_1k[:]
    testArr2 = reverse_sort_1k[:]
    testArr3 = random_1k[:]
    _test(testArr1, median_finding_randomized)
    _test(testArr2, median_finding_randomized)
    _test(testArr3, median_finding_randomized)

    testArr1 = positive_sort_1k[:]
    testArr2 = reverse_sort_1k[:]
    testArr3 = random_1k[:]
    _test(testArr1, median_finding_sort)
    _test(testArr2, median_finding_sort)
    _test(testArr3, median_finding_sort)

