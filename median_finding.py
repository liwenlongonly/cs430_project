# -*- coding: utf-8 -*-
# @Time : 2020/7/25 12:58
# @Author : ilong
# @Site :
# @File : median_finding.py
# @Software: PyCharm
import random


def partition(a, p, r):
    x = a[r]
    i = p - 1
    for j in range(p, r):
        if a[j] <= x:
            i += 1
            a[i], a[j] = a[j], a[i]
        # print("i:%d,j:%d" % (i, j))
        # print(a)
    a[i+1], a[r] = a[r], a[i+1]
    return i+1


def randomized_partition(a, p, r):
    i = random.randint(p, r)
    # print("random:%d value:%d" %(i, a[i]))
    a[i], a[r] = a[r], a[i]
    return partition(a, p, r)


def median_finading(a, p, r, i):
    """
    :param a: input array
    :param p: the left edge of the array, [0...
    :param r: the right edge of the array ...len(array) - 1]
    :param i: i-th smallest number, value range starts from 1
    """
    if p == r:
        return a[p]
    q = randomized_partition(a, p, r)
    k = q - p + 1
    if i == k:
        return a[q]
    elif i < k:
        return median_finading(a, p, q-1, i)
    else:
        return median_finading(a, q+1, r, i-k)


if __name__ == '__main__':
    array = [11, 20, 6, 5, 7, 9, 8, 10, 43, 77, 101, 88, 0]
    print(array)
    print(median_finading(array, 0, len(array) - 1, 1))  # min
    print(median_finading(array, 0, len(array) - 1, 4))
    print(median_finading(array, 0, len(array) - 1, 7))  # median
    print(median_finading(array, 0, len(array) - 1, 9))
    print(median_finading(array, 0, len(array) - 1, len(array)))  # max
