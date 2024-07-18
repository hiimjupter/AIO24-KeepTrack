class MyQueue():
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.__items = []

    def is_empty(self):
        return len(self.__items) == 0

    def is_full(self):
        return len(self.__items) == self.capacity

    def dequeue(self):
        if not self.is_empty():
            return f'You just eliminate {self.__items.pop(0)} out of Queue'
        else:
            return 'Queue is empty'

    def enqueue(self, value):
        if not self.is_full():
            self.__items.append(value)
            return f'You just add {value} into Queue'
        else:
            return 'Queue is full'

    def front(self):
        return f'Front value of Queue is {self.__items[0]}'


# Test case
queue1 = MyQueue(5)

print(queue1.enqueue(1))
print(queue1.enqueue(2))

print(queue1.is_full())

print(queue1.front())

print(queue1.dequeue())

print(queue1.front())

print(queue1.dequeue())

print(queue1.is_empty())
