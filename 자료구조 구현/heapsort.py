class BinaryMinHeap:
    def __init__(self):
        self.items = None

    def __len__(self):
        return len(self.items) - 1

    def insert(self, k):
        self.items.append(k)
        self.percolate_up()

    def percolate_up(self):
        cur = len(self)
        parent = cur // 2

        while parent > 0:
            if self.items[cur] < self.items[parent]:
                self.items[cur], self.items[parent] = self.items[parent], self.items[cur]

            cur = parent
            parent = cur // 2

    def extract(self):
        if len(self) < 1:
            return None

        root = self.items[1]
        self.items[1] = self.items[-1]
        self.items.pop()
        self.percolate_down(1)

        return root

    def percolate_down(self, cur):
        smallest = cur
        left = cur * 2
        right = cur * 2 + 1
        if left <= len(self) and self.items[left] < self.items[smallest]:
            smallest = left

        if right <= len(self) and self.items[right] < self.items[smallest]:
            smallest = right

        if cur != smallest:
            self.items[cur], self.items[smallest] = self.items[smallest], self.items[cur]
            self.percolate_down(smallest)

def sorted_by_heap(lst):
    maxheap = BinaryMinHeap
    for elem in lst:
        maxheap.insert(elem)

    desc = [maxheap.extract() for _ in range(len(lst))]
    return list(reversed(desc))