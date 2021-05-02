# 提供给 LRU HashMap 使用
class LRUListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.hashNext = None
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.key) + " " + str(self.val)
