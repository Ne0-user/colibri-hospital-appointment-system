class PQueue:
    def __init__(self, data):
        self.buffer = []
        try:
            for d in data:
                self.buffer.append(d)
        except:
            self.buffer.append(data)
        
    def enqueue(self, data):
        self.buffer.append(data)
        self.buffer.sort()
        
    def dequeue(self):
        if self.is_empty():
            raise Exception("dequeue from empty queue")
        return self.buffer.pop(0)
        
    def is_empty(self):
        return not self.buffer
    
    def peek(self):
        return self.buffer[0]
    
    def __len__(self):
        return len(self.buffer)
    
    def __repr__(self):
        return str(self.buffer)
    

import random
pq = PQueue(random.sample(range(0, 10), 7))
print(pq)
while not pq.is_empty():
    print(pq.dequeue())
print("cola vacia")