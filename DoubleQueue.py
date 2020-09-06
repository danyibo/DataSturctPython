class Queue:
    def __init__(self):
        self.items = []

    def __str__(self):
        queue = "<" + str(self.items) + ">"
        return queue

    def __len__(self):
        return len(self.items)

    def is_empty(self):
        return self.items == []

    def add_front(self, item):
        self.items.append(item)

    def add_rear(self, item):
        self.items.insert(0, item)

    def remove_front(self):
        return self.items.pop()

    def remove_rear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)


if __name__ == '__main__':
    double_queue = Queue()
    print(double_queue.is_empty())
    double_queue.add_front(0)
    double_queue.add_front(9)
    double_queue.add_rear(100)
    print(double_queue)
    print(double_queue.is_empty())
    print(len(double_queue))
    double_queue.remove_front()
    print(double_queue)
    double_queue.remove_rear()
    print(double_queue)