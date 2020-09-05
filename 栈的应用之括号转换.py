from DataStructPython.Stack import Stack


def pre_checker(symbol_string):
    """
    输入一个括号字符串，利用栈来判断这些括号是非是匹配的
    这是一个简单的栈的应用
    :param symbol_string:
    :return:
    """
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbol_string) and balanced:
        symbol = symbol_string[index]
        if symbol == "(" :
            s.push(symbol)
        else:
            if s.is_empty():
                balanced = False
            else:
                s.pop()
        index = index + 1
    if balanced and s.is_empty():
        return True
    else:
        return False


print(pre_checker("(((("))
