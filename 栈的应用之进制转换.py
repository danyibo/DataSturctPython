from DataStructPython.Stack import Stack


def divided_by_two(number):
    """
    10 进制转为 2 进制

    :param number: 一个十进制的数字
    :return: 二进制的数字
    """
    rem_stack = Stack()
    while number > 0:
        rem = number % 2
        rem_stack.push(rem)
        number = number // 2

    bin_string = ""
    while not rem_stack.is_empty():
        bin_string = bin_string + str(rem_stack.pop())

    return bin_string


def base_converter(dec_number, base):
    """
    十进制转为任意进制的数字
    :param dec_number: 十进制数
    :param base: 任意进制，如八进制，十六进制等
    :return: 返回转换后的数字
    """
    digits = "0123456789ABCDEF"
    rem_stack = Stack()
    while dec_number > 0:
        rem = dec_number % base
        rem_stack.push(rem)
        dec_number = dec_number // base

    new_string = ""
    while not rem_stack.is_empty():
        new_string = new_string + digits[rem_stack.pop()]

    return new_string


if __name__ == '__main__':
    print(divided_by_two(42))
    print(base_converter(42, 2))
    print(base_converter(42, 16))