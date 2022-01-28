class BinaryMaxHeap:
    def __init__(self):
        self.items = None

    def __len__(self):
        return len(self.items) - 1

    def insert(self, k):
        self.items.append(k)
        self._percolate_up()

    def _percolate_up(self):
        cur = len(self)
        parent = cur // 2
        while parent > 0:
            if self.items[cur] > self.items[parent]:
                self.items[cur], self.items[parent] = self.items[parent], self.items[cur]

            cur = parent
            parent = cur // 2

    def extract(self):
        if len(self) < 1:
            return None

        root = self.items[1]
        self.items[1] = self.items[-1]
        self.items.pop()
        self._percolate_down(1)

        return root

    def _percolate_down(self, cur):
        biggest = cur
        left = cur * 2
        right = cur * 2 + 1
        if left <= len(self) and self.items[biggest] < self.items[left]:
            biggest = left

        if right <= len(self) and self.items[biggest] < self.items[right]:
            biggest = right

        if biggest != cur:
            self.item[cur], self.item[biggest] = self.item[biggest], self.item[cur]
            self._percolate_down(biggest)


