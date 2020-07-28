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
                ***** Main Menu *****
---------------------------------------------------------
    1. Median of groups of 3,5 and 7
    2. Randomized median finding algorithm
    3. Quick Sort choose random element in the array as the pivot
    4. Quick Sort choose median in the array as the pivot
    5. Quit

---------------------------------------------------------

[*] Press Choice 1-5: """
median_prompt = "-------------------- Median of groups of 3,5 and 7 -----------------------"
random_median_prompt = "-------------------- Randomized median finding algorithm -----------------------"
median_sort_prompt = "-------------------- Quick Sort choose random element as pivot  -----------------------"
random_sort_prompt = "-------------------- Quick Sort choose median as  pivot  ---------------"
other_prompt = """
1. Hand Input Array
2. Auto Random Array
3. Back Menu
4. Quit
[*] Press Choice 1-4:  """

input_array_prompt = """
Input array example: 11 20 6 5 7 9 8 10 43 77 101 88 0
[*] Median Search, Please input array: """

random_array_prompt = """
generate random array......
Array is: {0}"""

auto_generate_count = "Please input Auto Generate Array's Element Count:"

end_string = "程序执行结束，欢迎下次访问....."
error_choice_string = '请输入正确的选择......'