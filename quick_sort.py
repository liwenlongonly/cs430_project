#!/usr/bin/python
# -*- coding: UTF-8 -*- 
import random
from median_finding import median_finding_randomized
from common import print_execute_time


class QuickSort:

    def quickSort(self, n, type="random"):
        self.n = n
        self.type_ = type
        self._quickSort(self.n, 0, len(n) - 1)
        return self.n

    def partition(self, n, p, r):
        # random 代表使用随机数来进行快速排序
        # median 代表使用中值来进行快速排序
        # 不传   代表使用数组最后一个值的正常快速排序

        if str(self.type_) == "random":
            random_x = random.randint(p, r - 1)
            temp = n[random_x]
            n[random_x] = n[r]
            n[r] = temp
        if str(self.type_) == "median":
            n[r] = median_finding_randomized(n, p, r, int((r - p) / 2 + 1))

        x = n[r]
        i = p - 1
        for j in range(p, r):

            if n[j] <= x:
                i += 1
                temp = n[i]
                n[i] = n[j]
                n[j] = temp

        temp = n[i + 1]
        n[i + 1] = n[r]
        n[r] = temp
        return i + 1

    def _quickSort(self, n, p, r):
        if p < r:
            q = self.partition(n, p, r)
            self._quickSort(n, p, q - 1)
            self._quickSort(n, q + 1, r)


if __name__ == '__main__':
    from test_data import *


    @print_execute_time
    def _quick_sort_test(n, type="random"):
        obj_ = QuickSort()
        return obj_.quickSort(n, type)


    # print("quick sort random >>>>>>>>>>>>>>>")
    # testArr1 = positive_sort_1k[:]
    # testArr2 = reverse_sort_1k[:]
    # testArr3 = random_1k[:]
    # print(_quick_sort_test(testArr1, "random"))
    # print(_quick_sort_test(testArr2, "random"))
    # print(_quick_sort_test(testArr3, "random"))

    # print("quick sort median >>>>>>>>>>>>>>>")
    # testArr1 = positive_sort_1k[:]
    # testArr2 = reverse_sort_1k[:]
    # testArr3 = random_1k[:]
    # print(_quick_sort_test(testArr1, "median"))
    # print(_quick_sort_test(testArr2, "median"))
    # print(_quick_sort_test(testArr3, "median"))

    print("quick sort random >>>>>>>>>>>>>>>")
    testArr4 = random_1k[:]
    testArr5 = random_5k[:]
    testArr6 = random_10k[:]
    testArr7 = random_15k[:]
    testArr8 = random_20k[:]
    testArr9 = random_25k[:]
    # print(_quick_sort_test(testArr4, "random"))
    # print(_quick_sort_test(testArr5, "random"))
    # print(_quick_sort_test(testArr6, "random"))
    # print(_quick_sort_test(testArr7, "random"))
    # print(_quick_sort_test(testArr8, "random"))
    print(testArr9)
    print(_quick_sort_test(testArr9, "random"))

    print("quick sort median >>>>>>>>>>>>>>>")
    testArr4 = random_1k[:]
    testArr5 = random_5k[:]
    testArr6 = random_10k[:]
    testArr7 = random_15k[:]
    testArr8 = random_20k[:]
    testArr9 = random_25k[:]
    # print(_quick_sort_test(testArr4, "median"))
    # print(_quick_sort_test(testArr5, "median"))
    # print(_quick_sort_test(testArr6, "median"))
    # print(_quick_sort_test(testArr7, "median"))
    # print(_quick_sort_test(testArr8, "median"))
    print(testArr9)
    print(_quick_sort_test(testArr9, "median"))
