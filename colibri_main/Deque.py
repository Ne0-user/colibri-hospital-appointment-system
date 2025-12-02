class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class Deque:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def __iter__(self):
        current = self.front
        while current:
            yield current.data
            current = current.next

    def is_empty(self):
        return self.size == 0

    def __len__(self):
        return self.size


    def append(self, data):
        new = Node(data)

        if self.is_empty():
            self.front = self.rear = new
        else:
            new.prev = self.rear
            self.rear.next = new
            self.rear = new

        self.size += 1

    def appendleft(self, data):
        new = Node(data)

        if self.is_empty():
            self.front = self.rear = new
        else:
            new.next = self.front
            self.front.prev = new
            self.front = new

        self.size += 1


    def pop(self):
        if self.is_empty():
            raise Exception("Deque vacío")

        data = self.rear.data

        self.rear = self.rear.prev
        if self.rear is None:
            self.front = None
        else:
            self.rear.next = None

        self.size -= 1
        return data

    def popleft(self):
        if self.is_empty():
            raise Exception("Deque vacío")

        data = self.front.data

        self.front = self.front.next
        if self.front is None:
            self.rear = None
        else:
            self.front.prev = None

        self.size -= 1
        return data


    def clear(self):
        self.front = None
        self.rear = None
        self.size = 0

    def to_list(self):
        return [item for item in self]

    def __repr__(self):
        return str(self.to_list())
