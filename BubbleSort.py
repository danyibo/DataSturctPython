def bubble_sort(a_list):
    for pass_num in range(len(a_list)-1, 0, -1):  # pass_num 为排序的趟数
        for i in range(pass_num):  # 选择元素
            if a_list[i] > a_list[i+1]:  # 如果这个元素比后面的元素大，就调换这两个元素的位置
                temp = a_list[i]
                a_list[i] = a_list[i+1]
                a_list[i+1] = temp


def bubbleSort(a_list):
    """
    对冒泡排序进行优化，即如果不交换就直接退出
    :param a_list:
    :return:
    """
    exchanges = True
    passnum = len(a_list) - 1
    while passnum > 0 and exchanges:
        for i in range(passnum):
            if a_list[i] > a_list[i+1]:
                exchanges = True
                temp = a_list[i]
                a_list[i] = a_list[i+1]
                a_list[i+1] = temp
        passnum -= 1

if __name__ == '__main__':
    a_list = [4, 5, 3, 1, 9, 100, 99, 0, 6]
    # bubble_sort(a_list)
    # print(a_list)
    bubbleSort(a_list)
    print(a_list)