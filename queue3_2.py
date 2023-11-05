class MyCircularDeque:

    def __init__(self, k: int):
        self.capacity = k
        self.deque = []
        

    def insertFront(self, value: int) -> bool:
        if len(self.deque) < self.capacity:
            self.deque = [value] + self.deque
            return True
        else:
            return False

    def insertLast(self, value: int) -> bool:
        if len(self.deque) < self.capacity:
            self.deque.append(value)
            return True
        else:
            return False

    def deleteFront(self) -> bool:
        if self.deque:
            self.deque.pop(0)
            return True
        else:
            return False

    def deleteLast(self) -> bool:
        if self.deque:
            self.deque.pop()
            return True
        else:
            return False

    def getFront(self) -> int:
        if self.deque:
            return self.deque[0]
        else:
            return -1

    def getRear(self) -> int:
        if self.deque:
            return self.deque[-1]
        else:
            return -1

    def isEmpty(self) -> bool:
        return len(self.deque) == 0

    def isFull(self) -> bool:
        return len(self.deque) == self.capacity
    
circular_deque = MyCircularDeque(3)
print(circular_deque.insertLast(1))  
print(circular_deque.insertLast(2))  
print(circular_deque.insertFront(3)) 
print(circular_deque.insertFront(4)) 
print(circular_deque.getRear())      
print(circular_deque.isFull())       
print(circular_deque.deleteLast())   
print(circular_deque.insertFront(4)) 
print(circular_deque.getFront())     