def binary_search(a_list, item):
    first = 0
    last = len(a_list) - 1
    found = False

    while first <= last and not found:
        mid_point = (first + last) // 2
        if a_list[mid_point] == item:
            found = True
        else:
            if item < a_list[mid_point]:
                last = mid_point - 1
            else:
                first = mid_point + 1
    return found


def binary_search_recursion(a_list, item):
    if len(a_list) == 0:
        return False
    else:
        mid_point = len(a_list) // 2
        if a_list[mid_point] == item:
            return True
        else:
            if item < a_list[mid_point]:
                return binary_search_recursion(a_list[:mid_point], item)
            else:
                return binary_search_recursion(a_list[mid_point+1:], item)


if __name__ == '__main__':
    test_list = [0, 1, 2, 3, 4, 19, 45, 99, 101]
    print(binary_search(test_list, 5))
    print(binary_search(test_list, 4))
    print(binary_search_recursion(test_list, 5))
    print(binary_search_recursion(test_list, 19))