"""Queue represented by a Python list"""


class Queue:
    """
    Queue: an element first en_quequ in queue, and this element first out of queue
    first in, first out

    Stack: last in, first out
    """
    def __init__(self):
        self.entries = []
        self.length = 0
        self.front = 0

    def __len__(self):
        return self.length

    def __str__(self):
        """打印队列的方式"""
        printed = "<" + str(self.entries)[1:-1] + ">"
        return printed

    def en_queue(self, item):
        self.entries.append(item)
        self.length = self.length + 1

    def de_queue(self):
        self.length = self.length - 1
        dequeued = self.entries[self.front]  # 将第一个元素出队
        self.entries = self.entries[1:]
        return dequeued

    def queue_front(self):
        return self.entries[0]

    def size(self):
        return self.length


if __name__ == '__main__':
    q = Queue()
    q.en_queue(1)
    q.en_queue(3)
    q.en_queue(2)
    print(q)
    print("出队的元素为 {}". format(q.de_queue()))
    print("队列的长度为 {}".format(len(q)))
    print("用方法获得队列的元素 {}".format(q.size()))
