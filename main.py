import os
from median_finding import median_finading
from prompt import *


def main():
    key = input(introduce)
    if key:
        os.system('cls')
    while True:
        choice = input(menu)
        if choice in ('1', 'm', 'M'):
            str_array = input(median_prompt)
            array = [int(item) for item in str_array.split()]
            result = median_finading(array, 0, len(array) - 1, 1)
            result_string = median_result.format(str_array, result)
            print(result_string)
        elif choice in ('2', 's', 'S'):
            while True:
                sort_choice = input(quicksort_prompt)
                if sort_choice in ('1', 'r', 'R'):
                    print("快速排序选择随机值....")
                elif sort_choice in ('2', 'm', 'M'):
                    print("快速排序选择中位数.....")
                elif sort_choice in ('3', 'b', 'B'):
                    print("正在进入主菜单..........")
                    break
                elif sort_choice in ('4', 'q', 'Q'):
                    print("程序执行结束，欢迎下次访问.....")
                    exit()
        elif choice in ('3', 'h', 'H'):
            print(help)
        elif choice in ('4', 'q', 'Q'):
            exit()
            print("程序执行结束，欢迎下次访问.....")
        else:
            print("请输入正确的选择......")


if __name__ == '__main__':
    main()
