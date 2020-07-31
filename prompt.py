"""
代码提示信息存储位置
"""

COLOR_START = "\033[0;"
COLOR_END = "\033[0m"
colors = {
    'black': '30m',
    'red': '31m',
    'green': '32m',
    'yellow': '33m',
    'blue': '34m',
    'cyan': '36m',  # 青色
}


def color_string(string, color='blue'):
    """if color not in dict, default color is black"""
    return COLOR_START + colors.get(color, '30m') + string + COLOR_END


# back_prompt = "正在返回主菜单......"
back_prompt = "Backing Main Menu......"
introduce = """
---------------------------------------------------------
                ***** Project Introduce *****
---------------------------------------------------------
    Name: Median finding, Order Statistics and Quick Sort
    Version: 0.1
    Date: 2020-7-26
    Author: Hao Liu, WenLong Li, Fan Guo
    Color Explain:
        Main Menu: Green
        Sub Menu: cyan
        Prompt: blue
        error output: red

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
median_sort_prompt = "-------------------- Quick Sort choose median as  pivot  ---------------"
random_sort_prompt = "-------------------- Quick Sort choose random element as pivot  -----------------------"
other_prompt = """
1. Hand Input Array
2. Auto Random Array
3. Back Menu
4. Quit
[*] Press Choice 1-4:  """

input_array_prompt = """
Input array example: 11 20 6 5 7 9 8 10 43 77 101 88 0
[*] Please input array: """

random_array_prompt = """
generate random array......
Array is: {0}"""

auto_generate_count = "Please input Auto Generate Array's Element Count:"

# end_string = "程序执行结束，欢迎下次访问....."
end_string = "Exiting Project, Welcome to access next time....."
# error_choice_string = '请输入正确的选择......'
error_choice_string = 'Please input correct choice!!!'
