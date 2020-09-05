# __author__ = "Omkar Pathak"


class Stack:
    """
    A stack is an abstract data type that serves as a collection of
    elements with tow principal operation:
    push() and pop()
    push() adds an element to the top of stack, and pop() removes an
    elements from top of a stack.
    The order in which elements come off of a stack are
    Last In, First Out(LIFO)

    dan：using list to do that！

    """
    def __init__(self, limits=10):
        self.stack = []
        self.limits = limits

    def __bool__(self):
        return bool(self.stack)

    def __str__(self):
        return str(self.stack)

    def push(self, data):
        if len(self.stack) >= self.limits:
            raise StackOverflowError
        self.stack.append(data)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            raise IndexError("pop from an empty stack")

    def peek(self):
        if self.stack:
            return self.stack[-1]

    def is_empty(self):
        return not bool(self.stack)

    def size(self):
        return len(self.stack)

    def __contains__(self, item) -> bool:
        """Check if item is in stack"""
        return item in self.stack


class StackOverflowError(BaseException):
    pass


if __name__ == '__main__':
    stack = Stack()
    for i in range(10):
        stack.push(i)
    print(stack)
    # stack.push(10)
    pop_element = stack.pop()
    print("pop an element is {}".format(pop_element))
    print("peek element is {} ".format(stack.peek()))
    print("size of the stack is {}".format(stack.size()))
    print(stack.is_empty())

