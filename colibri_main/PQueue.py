class PriorityQueue:
    def __init__(self):
        self.heap = []

    def insert(self, item, priority):
        self.heap.append((priority, item))
        self._heapify_up(len(self.heap) - 1)

    def pop(self):
        if not self.heap:
            return None
        self._swap(0, len(self.heap) - 1)
        priority, item = self.heap.pop()
        self._heapify_down(0)
        return item

    def peek(self):
        return self.heap[0][1] if self.heap else None

    def _heapify_up(self, index):
        parent = (index - 1) // 2
        while index > 0 and self.heap[index][0] < self.heap[parent][0]:
            self._swap(index, parent)
            index = parent
            parent = (index - 1) // 2

    def _heapify_down(self, index):
        child = 2 * index + 1
        while child < len(self.heap):
            right = child + 1
            if right < len(self.heap) and self.heap[right][0] < self.heap[child][0]:
                child = right
            if self.heap[index][0] <= self.heap[child][0]:
                break
            self._swap(index, child)
            index = child
            child = 2 * index + 1

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def is_empty(self):
        return len(self.heap) == 0
