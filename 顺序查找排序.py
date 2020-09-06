def sequential_search(a_list, item):
    pos = 0
    found = False

    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos += 1

    return found


if __name__ == '__main__':
    test_list = [2, 1, 34, 5, 6, 7, 3]
    print(sequential_search(test_list, 5))
    print(sequential_search(test_list, 100))