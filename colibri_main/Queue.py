class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Queue:
    def __init__(self, data=None):
        self.front = None
        self.rear = None
        self.size = 0
        
        if data:
            try:
                for d in data:
                    self.enqueue(d)
            except:
                self.enqueue()
                
    def enqueue(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
            self.size +=1
            
    def dequeue(self):
        if self.is_empty():
            raise Exception("Dequeue from empty queue")
            
        data_out = self.front.data
        self.front = self.fron.next
        if self.front == None:
            self.rear = None
            
        self.size -=1
            
        return data_out
    
    def peek(self):
        if self.is_empty():
            raise Exception("Peek from empty queue")
            
        return self.front.data
    
    def length(self):
        return self.size
    
        
    def is_empty(self):
        return self.front == None
    
    def __repr__(self):
        current = self.front
        while current:
            print(current.data, end=", ")
            current = current.next
            
        return"\b\b "
    
    
q=Queue([11, 22, 33, 44, 55])
print(q)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    