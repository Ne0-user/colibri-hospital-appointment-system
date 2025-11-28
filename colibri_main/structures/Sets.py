class Set:
    def __init__(self):
        self.__capacity = 10
        self.__size = 0
        self.__buckets = [[] for _ in range(self.__capacity)]
        
    def add(self, element):
        bucket_index = self.__hash(element)
        bucket = self.__buckets[bucket_index]
        
        if element not in bucket:
            bucket.append(element)
            self.__size += 1
        
        if self.__size > self.__capacity * 0.7:
            self.__resize()
    
    def __hash(self, element, base=None):
        if not base:
            base = self.__capacity
            
        return hash(element) % base
    
    def __resize(self):
        new_capacity = self.__capacity * 2
        new_buckets = [[] for _ in range(new_capacity)]
        for b in self.__buckets:
            for e in b:
                bucket_index = self.__hash(e, new_capacity)
                new_buckets[bucket_index].append(e)
        
        self.__capacity = new_capacity
        self.__buckets = new_buckets
        
    def remove(self, element):
        bucket_index = self.__hash(element)
        bucket = self.__buckets[bucket_index]
        
        if element not in bucket:
            raise KeyError(f"{element}")
        
        bucket.remove(element)
        self.__size -= 1
        
    def discard(self, element):
        bucket_index = self.__hash(element)
        bucket = self.__buckets[bucket_index]
        if element in bucket:
            bucket.remove(element)
            self.__size -= 1
        
    def pop(self):
        if self.is_empty():
            raise Exception("pop from empty Set")
            
        pass
        return #pop()
    
    def claer(self):
        self.__capacity = 10
        self.__size = 0
        self.__buckets = [[] for _ in range(self.__capacity)]
        
    def copy(self):
        new_set = Set()
        for b in self.__buckets:
            for e in b:
                new_set.add(e)
                
        return new_set
        
    def is_empty(self):
        return self.__size == 0
    
    """TEORIA DE CONJUNTOS"""
    def union(self, s2):#'|' OR
        new_set = Set()
        
        for e in self:
            new_set.add(e)
        
        for e in s2:
            new_set.add(e)
            
        return new_set

    def __iter__(self):
        for b in self.__buckets:
            for e in b:
                yield e
        
    def intersection(self, s2):
        new_set = Set()
        for e in self:
            if e in s2:# if s2.__contains__(e)
                new_set.add(e)
        
        return new_set
    
    def __or__(self, s2):
        return self.union(s2)
    
    def __and__(self, s2):
        return self.intersection(s2)
    
    def __contains__(self, element):
        for e in self:
            if e == element:
                return True
            
    def __str__(self):
        print("{", end="")
        for e in self:
            print(e, end=", ")
        return "}" if self.is_empty() else "\b\b}"
    
    
if __name__ == "__main__":
    import random
    s1 = Set()
    for e in random.sample(range(0, 10), 7):
        s1.add(e)
        
    s2 = Set()
    for e in random.sample(range(0, 10), 7):
        s2.add(e)
        
    print(s1.union(s2))
    print(s1 | s2)
    
    print(s1.intersection(s2))
    print(s1 & s2)












