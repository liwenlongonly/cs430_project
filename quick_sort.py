#!/usr/bin/python
# -*- coding: UTF-8 -*- 
import random
from median_finding import median_finding_randomized
from common import print_execute_time
import time
import sys
sys.setrecursionlimit(1000000)


class QuickSort:

    def __init__(self):
        self.t_median_=0
        self.t_all=0

    def quickSort(self, n, type="random"):
        tmp = time.time()
        self.n = n
        self.type_ = type
        self._quickSort(self.n, 0, len(n) - 1)
        self.t_all = time.time() - tmp
        return self.n, self.t_all - self.t_median_

    def partition(self, n, p, r):
        # random 代表使用随机数来进行快速排序
        # median 代表使用中值来进行快速排序

        if str(self.type_) == "random":
            random_x = random.randint(p, r)
            temp = n[random_x]
            n[random_x] = n[r]
            n[r] = temp
            x = n[r]
            i = p - 1
            
            for j in range(p, r):

                if n[j] <= x:
                    i += 1
                    temp = n[i]
                    n[i] = n[j]
                    n[j] = temp

            temp = n[i + 1]
            n[i + 1] = x
            n[r] = temp
            return i + 1
        if str(self.type_) == "median":
            t_median_=time.time()
            x = median_finding_randomized(n, p, r, int((r - p + 1) / 2))
            self.t_median_+=time.time()-t_median_
            i = p - 1
            
            for j in range(p, r):

                if n[j] <= x:
                    i += 1
                    temp = n[i]
                    n[i] = n[j]
                    n[j] = temp

            return i

    def _quickSort(self, n, p, r):
        if p < r:
            q = self.partition(n, p, r)
            self._quickSort(n, p, q - 1)
            self._quickSort(n, q + 1, r)



#@print_execute_time
def quick_sort_test(n, type="random"):
    obj_ = QuickSort()
    result, time =  obj_.quickSort(n, type)
    print("execute time:%0.2f ms" % (time * 1000))
    return result


if __name__ == '__main__':
    from test_data import *

    print("quick sort random >>>>>>>>>>>>>>>")
    testArr1 = positive_sort_1k[:]
    testArr2 = reverse_sort_1k[:]
    testArr3 = random_1k[:]
    quick_sort_test(testArr1, "random")
    quick_sort_test(testArr2, "random")
    quick_sort_test(testArr3, "random")

    print("quick sort median >>>>>>>>>>>>>>>")
    testArr1 = positive_sort_1k[:]
    testArr2 = reverse_sort_1k[:]
    testArr3 = random_1k[:]
    quick_sort_test(testArr1, "median")
    quick_sort_test(testArr2, "median")
    quick_sort_test(testArr3, "median")

    print("quick sort random >>>>>>>>>>>>>>>")
    testArr4 = random_1k[:]
    testArr5 = random_5k[:]
    testArr6 = random_10k[:]
    testArr7 = random_15k[:]
    testArr8 = random_20k[:]
    testArr9 = random_25k[:]
    quick_sort_test(testArr4, "random")
    quick_sort_test(testArr5, "random")
    quick_sort_test(testArr6, "random")
    quick_sort_test(testArr7, "random")
    quick_sort_test(testArr8, "random")
    quick_sort_test(testArr9, "random")

    print("quick sort median >>>>>>>>>>>>>>>")
    testArr4 = random_1k[:]
    testArr5 = random_5k[:]
    testArr6 = random_10k[:]
    testArr7 = random_15k[:]
    testArr8 = random_20k[:]
    testArr9 = random_25k[:]
    quick_sort_test(testArr4, "median")
    quick_sort_test(testArr5, "median")
    quick_sort_test(testArr6, "median")
    quick_sort_test(testArr7, "median")
    quick_sort_test(testArr8, "median")
    quick_sort_test(testArr9, "median")
