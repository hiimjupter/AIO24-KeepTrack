class MyStack():
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.__items = []

    def is_empty(self):
        return len(self.__items) == 0

    def is_full(self):
        return len(self.__items) == self.capacity

    def pop(self):
        if not self.is_empty():
            return f'You just eliminate {self.__items.pop(-1)} out of Stack'
        else:
            return 'Stack is empty'

    def push(self, value):
        if not self.is_full():
            self.__items.append(value)
            return f'You just add {value} into Stack'
        else:
            return 'Stack is full'

    def top(self):
        return f'Top value of Stack is {self.__items[-1]}'


# Test case
stack1 = MyStack(5)

print(stack1.push(1))
print(stack1.push(2))

print(stack1.is_full())

print(stack1.top())

print(stack1.pop())

print(stack1.top())

print(stack1.pop())

print(stack1.is_empty())
