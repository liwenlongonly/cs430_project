"""
代码提示信息存储位置
"""
back_prompt = "正在返回主菜单......"
introduce = """
---------------------------------------------------------
                ***** Project Introduce *****
---------------------------------------------------------
    Name: Median finding, Order Statistics and Quick Sort
    Version: 0.1
    Date: 2020-7-26
    Author: Hao Liu,  WenLong Liu, Fan Guo

---------------------------------------------------------
[*] Press any key enter  menu ......"""

menu = """
---------------------------------------------------------
                ***** Menu *****
---------------------------------------------------------
    1. (m)Median Finding
    2. (s)Quick sort
    3. (h)Help
    4. (q)Quit

---------------------------------------------------------

[*] Press Choice 1-4 or m|s|h|q ......"""
help = """
---------------------------------------------------------
                ***** Help *****
---------------------------------------------------------
    1. (m)Median Finding - Press 1 or m or M
    2. (s)Quick sort     - Press 2 or s or S
    3. (h)Help           - Press 3 or h or H
    4. (q)Quit           - Press 4 or q or Quit

---------------------------------------------------------

"""

median_prompt = """
-------------------- Median Search ----------------------
Input array example: 11 20 6 5 7 9 8 10 43 77 101 88 0
[*] Median Search, Please input array: """

median_result = """
******************* Median Result ***********************
Success: Find Array {0} Median is {1}. 
"""

quicksort_prompt = """
-------------------- Quick Sort -----------------------
Input array example: 11 20 6 5 7 9 8 10 43 77 101 88 0
    1. (r)Choose a random element in the array as the pivot
    2. (m)Choose median in the array as the pivot
    3. (b) Back Menu
    4. (q) Quit
---------------------------------------------------------
[*] Press Choice 1-4 or r|m|b|p......"""


def cls():
    print("\n" * 20)
