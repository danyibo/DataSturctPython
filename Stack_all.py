"""
Stack operations using a doubly linked list
dan: 思考关于链表的实现


"""


class Node:
    def __init__(self, data):
        self.data = data  # assign data
        self.next = None  # Initialize next as null
        self.prev = None  # Initialize prev as null


class Stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        """add a node to stack"""
        if self.head is None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            new_node.prev = None
            self.head = new_node

    def pop(self):
        """pop the top element off the stack"""
        if self.head is None:
            return None  # empty stack
        else:
            temp = self.head.data
            self.head = self.head.next
            self.head.prev = None
            return temp

    def top(self):
        """return the top element of the stack"""
        return self.head.data

    def __len__(self):
        temp = self.head
        count = 0
        while temp is not None:
            count += 1
            temp = temp.next
        return count

    def is_empty(self):
        return self.head is None

    def print_stack(self):
        print("stack elements are: ")
        temp = self.head
        while temp is not None:
            print(temp.data, end="->")
            temp = temp.next


if __name__ == "__main__":

    # Start with the empty stack
    stack = Stack()

    # Insert 4 at the beginning. So stack becomes 4->None
    print("Stack operations using Doubly LinkedList")
    stack.push(4)

    # Insert 5 at the beginning. So stack becomes 4->5->None
    stack.push(5)

    # Insert 6 at the beginning. So stack becomes 4->5->6->None
    stack.push(6)

    # Insert 7 at the beginning. So stack becomes 4->5->6->7->None
    stack.push(7)

    # Print the stack
    stack.print_stack()

    # Print the top element
    print("\nTop element is ", stack.top())

    # Print the stack size
    print("Size of the stack is ", len(stack))

    # pop the top element
    stack.pop()

    # pop the top element
    stack.pop()

    # two elements have now been popped off
    stack.print_stack()

    # Print True if the stack is empty else False
    print("\nstack is empty:", stack.is_empty())
