from DataStructPython.Queue import Queue


def hot_potato(name_list, num):
    sim_queue = Queue()
    for name in name_list:
        sim_queue.en_queue(name)
    while sim_queue.size() > 1:
        for i in range(num):
            sim_queue.en_queue(sim_queue.de_queue())
        sim_queue.de_queue()

    return sim_queue.de_queue()


if __name__ == '__main__':
    print(hot_potato(name_list=["A", "C", "D", "F", "G"], num=2))