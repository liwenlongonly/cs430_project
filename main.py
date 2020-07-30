import os
from median_finding import median_finding_randomized_test, median_finding_right_test
from prompt import *
from test_data import create_random_array
from quick_sort import quick_sort_test

is_back = False

"""
主菜单显示为： 绿色
子菜单的显示为: 青色
输入提示为: 蓝色
错误的提示为: 红色
"""


def sub_choice_function(sub_prompt, func, type="median"):
    """
    :param sub_prompt: 子菜单的提示信息
    :param func: 子菜单执行的业务逻辑函数
    :param type: 子菜单的类型是找中位数还是排序(因为传递的参数不同),
                "median"代表寻找中位数
                "random-sort"代表随机数作为枢纽排序
                "median-sort"代表中位数作为枢纽排序
    :return:
    """
    while True:
        sub_choice = input(color_string(sub_prompt + other_prompt, color='cyan'))
        if sub_choice == '1':
            str_array = input(color_string(sub_prompt + input_array_prompt))
            array = [int(item) for item in str_array.split()]
            if type == 'median':
                result = func(array, 0, len(array) - 1, (len(array) + 1) // 2)
            elif type == 'median-sort':
                result = func(array, type="median")
                # quick_sort_test(array, type='median')
            elif type == 'random-sort':
                result = func(array, type="random")
                # quick_sort_test(array, type='random')
        elif sub_choice == '2':
            print(color_string(sub_prompt))
            count = int(input(color_string(auto_generate_count)))
            array = []
            create_random_array(array, count)
            print(color_string(random_array_prompt.format(array)))
            if type == 'median':
                result = func(array, 0, len(array) - 1, 1)
            elif type == 'median-sort':
                result = func(array, type="median")
            elif type == 'random-sort':
                result = func(array, type="random")
        elif sub_choice == '3':
            global is_back
            is_back = True
            break
        elif sub_choice == '4':
            print(color_string(end_string, color='green'))
            exit()
        else:
            print(color_string(error_choice_string, color='red'))


def main():
    key = input(introduce)
    # is_back = False
    while True:
        # 清空屏幕
        os.system("clear")
        if is_back:
            print(color_string(back_prompt, color='yellow'))
        choice = input(color_string(menu, color='green'))
        # 1. Median of groups of 3,5 and 7
        if choice == '1':
            sub_choice_function(median_prompt, median_finding_right_test)
        # 2. Randomized median finding algorithm
        elif choice == '2':
            sub_choice_function(random_median_prompt, median_finding_randomized_test)
        # 3. Quick Sort choose random element in the array as the pivot
        elif choice == '3':
            sub_choice_function(random_sort_prompt, quick_sort_test, type='random-sort')
        # 4. Quick Sort choose median in the array as the pivot
        elif choice == '4':
            sub_choice_function(median_sort_prompt, quick_sort_test, type='median-sort')
        elif choice == '5':
            print(color_string(end_string, color='green'))
            exit()
        else:
            print(color_string(error_choice_string, color='red'))

        # 如果是子菜单返回，不需要查询是否继续系统的运行，直接进入主菜单.
        if is_back:
            print(color_string(back_prompt, color='yellow'))
            continue
        # # 询问用户是否继续系统的执行
        # again = input("Continue Syetem?(Y|N)")
        # if again in ('Y', 'y', ''):
        #     continue
        # else:
        #     print(end_string)
        #     break


if __name__ == '__main__':
    main()
    # result = quick_sort_test([3, 2, 1], type='median')
    # print(result)
