class Map:
    def __init__(self):
        self.__items = []
        
    def put(self, key, value):
        for i, (k, v) in enumerate(self.__items):
            if k == key:
                self.__items[i] = (key, value)
                return
        self.__items.append((key, value))
        
    def get(self, key):
        for i, (k, v) in self.__items:
            if k == key:
                return v
        raise KeyError(f"key {key} not found")

    def remove(self, key):
        for i, (k, v) in enumerate(self.__items):
            if k == key:
                del self.__items[i]
                return
        raise KeyError(f"key {key} not found")
        
    def __comntains__(self, key):
        return any(k == key for k, v in self.__items)
    
    def __iter__(self):
        for k, v in self.__items:
            yield k, v
            
    def __len__(self):
        return len(self.__items)
    
    def clear(self):
        self.__items = []
        
    def keys(self):
        return [k for k, v in self.__items]
    
    def value(self):
        return [v for k, v in self.__items]
    
    def items(self):
        return [(k,v) for k, v in self.__items]
    
    def __str__(self):
        return "{"+ ", ".join(f"{k}: {v}" for k, v in self.__items)
    
class HashMap:
    def __init__(self, capacity=10, items=None):
        self.__capacity = capacity
        self.__size = 0
        self.__buckets = [[] for _ in range(self.__capacity)]
        
        if items:
            for k, v in items:
                self.put(k, v)
                
    def put(self, key, value):
        buckets_index = self.__hash(key)
        bucket = self.__buckets[buckets_index]
        
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return 
        bucket.append((key, value))
        self.__size +=1
        
        if self.__size > self.__capacity * 0.7:
            self.__resize()
    
    def __hash(self, key, base = None):
        if not base:
            base = self.__capacity
        return hash(key) % base
    
    def __resize(self):
        new_capacity = self.__capacity*2
        new_buckets = [[] for _ in range(new_capacity)]
        
        for b in self.__buckets:
            for k, v in b:
                new_bucket_index = self.__hash(k, new_capacity)
                new_buckets[new_bucket_index].append((k, v))
        self.__capacity = new_capacity
        self.__buckets = new_buckets
        
        
    def __get(self, key):
        bucket_index = self.__hash(key)
        bucket = self.__buckets[bucket_index]
        
        for k, v in bucket:
            if k == key:
                return v, True
        return None, False
    
    
    def get(self, key):
        v, found = self.__get(key)
        
        if found:
            return v
        
        raise KeyError(f"key {key} not found")
        
    def remove(self, key):
        bucket_index = self.__hash(key)
        bucket = self.__buckets[bucket_index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.__size -= 1
                return
        
        raise KeyError(f"key {key} not found")

        
    def __contains__(self, key):
        v, found = self.__get(key)
        return found
    
    def __iter__(self):
        for b in self.__buckets:
            for k , v in b:
                yield k, v
    
    def __len__(self):
        return self.__size
    
    def keys(self):
        return [k for k, v in self]
    
    def values(self):
        return [v for k, v in self]
    
    def items(self):
        return[(k, v) for k, v in self]
    
    def clear(self):
        self.__capacity = 10
        self.__size = 0
        self.__buckets = [[] for _ in range(self.__capacity)]
        
    def __str__(self):
        return "{" + ", ".join(f"{k}: {v}" for k, v in self)
    
    

if __name__ == "__main__":
    m = Map()
    
    m.put('5', 55)
    m.put('6', 66)
    m.put('7', 77)
    m.put('8', 88)
    m.put('9', 99)
    m.put('1', 66)
    m.put('2', 77)
    m.put('3', 88)
    m.put('4', 99)
    
    print(m)
    
    class Void:
        def __init__(self):
            self.algo = 10
            
    class Niente:
        pass
    
    m1 = HashMap()
    m1.put("Hola", "Mundo")
    m1.put("lista0", [_ for _ in range(9)])
    m1.put("lista1", [_ for _ in range(9)])
    m1.put("lista2", [_ for _ in range(9)])
    m1.put("lista3", [_ for _ in range(9)])
    m1.put("lista4", [_ for _ in range(9)])
    m1.put("lista5", [_ for _ in range(9)])
    m1.put("lista6", [_ for _ in range(9)])
    m1.put("lista7", [_ for _ in range(9)])
    m1.put("lista9", [_ for _ in range(9)])
    m1.remove("lista0")

    m1.put(Void(), Niente())
    
    m.put("Otro mapa", m1)
    
    print(m)
    