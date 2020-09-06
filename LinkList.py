class Node:
    def __init__(self, init_data):
        self.data = init_data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next


class UnorderList:
    def __init__(self):
        self.head = None

    def is_empyt(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.get_next()
        return count

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
        return found


if __name__ == '__main__':
    temp = Node(93)
    print(temp.get_data())
    my_list = UnorderList()
    print(my_list.is_empyt())
    my_list.add(9)
    my_list.add(10)
    print(my_list.is_empyt())
    print(my_list.size())
    print(my_list.search(9))
    print(my_list.search(100))