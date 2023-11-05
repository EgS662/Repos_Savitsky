from queue import Queue

class MyStack:

    def __init__(self):
        self.queue1 = Queue()
        self.queue2 = Queue()
        self.top_element = None

    def push(self, x):
        self.top_element = x
        self.queue2.put(x)
        while not self.queue1.empty():
            self.queue2.put(self.queue1.get())
        self.queue1, self.queue2 = self.queue2, self.queue1

    def pop(self):
        if not self.queue1.empty():
            popped = self.queue1.get()
            if not self.queue1.empty():
                self.top_element = self.queue1.queue[0]
            return popped

    def top(self):
        return self.top_element

    def empty(self):
        return self.queue1.empty()

my_stack = MyStack()
my_stack.push(1)
my_stack.push(2)
print(my_stack.top())  
print(my_stack.pop())  
print(my_stack.empty())  