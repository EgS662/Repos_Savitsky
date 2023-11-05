class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [None] * k
        self.capacity = k
        self.front = 0
        self.rear = -1
        self.size = 0

    def enQueue(self, value: int) -> bool:
        if not self.isFull():
            self.rear = (self.rear + 1) % self.capacity
            self.queue[self.rear] = value
            self.size += 1
            return True
        else:
            return False

    def deQueue(self) -> bool:
        if not self.isEmpty():
            self.front = (self.front + 1) % self.capacity
            self.size -= 1
            return True
        else:
            return False

    def Front(self) -> int:
        return self.queue[self.front] if not self.isEmpty() else -1

    def Rear(self) -> int:
        return self.queue[self.rear] if not self.isEmpty() else -1

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity
    
circular_queue = MyCircularQueue(3)
print(circular_queue.enQueue(1))  
print(circular_queue.enQueue(2))  
print(circular_queue.enQueue(3)) 
print(circular_queue.enQueue(4))  
print(circular_queue.Rear())     
print(circular_queue.isFull())    
print(circular_queue.deQueue())   
print(circular_queue.enQueue(4))  
print(circular_queue.Rear()) 