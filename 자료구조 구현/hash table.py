import collections


class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None

class MyHashTable:
    def __init__(self):
        self.size = 100
        self.table = collections.defaultdict(ListNode)

    def put(self, key, value):
        index = key % self.size

        new_node = ListNode(key, value)

        item = self.table(index)
        if not item:
            self.table[index] = new_node
        while item:
            if item.key == key:
                item.value = value
                return
            if not item.next:
                break
            item = item.next
        item.next = new_node

    def get(self, key):
        index = key % self.size
        if self.table[index].value is None:
            return -1

        p = self.table[index]
        while p:
            if p.key == key:
                return p.value
            p = p.next
        return -1

    def remove(self, key):
        index = key % self.size
        if self.table[index].value is None:
            return

        p = self.table[index]
        if p.key == key:
            self.table[index] = ListNode() if p.next is None else p.next
            return

        prev = p
        while p:
            if p.key == key:
                prev.next = p.next
                return
            prev, p = p, p.next