from DataStructPython.DoubleQueue import Queue


def pal_checker(a_string):
    char_queue = Queue()
    for ch in a_string:
        char_queue.add_rear(ch)
        still_equal = True

        while char_queue.size() > 1 and still_equal == True:
            first = char_queue.remove_front()
            last = char_queue.remove_rear()
            print(first, last)

            if first != last:
                still_equal = False

    return still_equal

if __name__ == '__main__':
    print(pal_checker(a_string="radar"))
    print(pal_checker(a_string="caa"))