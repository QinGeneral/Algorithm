class Node:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.head = Node()
        self.capacity = capacity
        self.curCap = 0

    def get(self, key: int) -> int:
        temp = self.head.next
        pre = self.head
        while temp:
            if temp.key == key:
                pre.next = temp.next
                temp.next = self.head.next
                self.head.next = temp
                return temp.val
            pre = pre.next
            temp = temp.next
        return -1

    def put(self, key: int, value: int) -> None:
        temp = self.head.next
        pre = self.head
        while temp:
            if temp.key == key:
                pre.next = temp.next
                temp.next = self.head.next
                self.head.next = temp
                temp.val = value
                return
            pre = pre.next
            temp = temp.next

        if self.curCap == self.capacity:
            temp = self.head
            while temp.next and temp.next.next:
                temp = temp.next
            temp.next = None
            self.curCap -= 1
        node = Node(key, value)
        node.next = self.head.next
        self.head.next = node
        self.curCap += 1

    def __str__(self):
        s = ""
        temp = self.head.next
        while temp:
            s += str(temp.key) + " " + str(temp.val) + "; "
            temp = temp.next
        return s


lRUCache = LRUCache(2)
print(lRUCache)
lRUCache.put(1, 1)
print(lRUCache)
# 缓存是 {1=1}
lRUCache.put(2, 2)
print(lRUCache)
# 缓存是 {1=1, 2=2}
lRUCache.get(1)
print(lRUCache)
# 返回 1
lRUCache.put(3, 3)
print(lRUCache)
# 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
lRUCache.get(2)
print(lRUCache)
# 返回 -1 (未找到)
lRUCache.put(4, 4)
print(lRUCache)
# 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
lRUCache.get(1)
print(lRUCache)
# 返回 -1 (未找到)
lRUCache.get(3)
print(lRUCache)
# 返回 3
lRUCache.get(4)
print(lRUCache)
# 返回 4


class Node:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

    def setPrev(self, node):
        self.prev = node
        node.next = self


class LRUCache:
    def __init__(self, capacity: int):
        self.head = Node()
        self.capacity = capacity
        self.curCap = 0
        self.map = {}

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1

        temp = self.map[key]
        if temp.next:
            temp.next.setPrev(temp.prev)
        else:
            temp.prev.next = None
        self.head.next.setPrev(temp)
        temp.setPrev(self.head)
        return temp.val

    def put(self, key: int, value: int) -> None:
        if key not in self.map:
            if self.curCap == self.capacity:
                temp = self.head
                while temp.next and temp.next.next:
                    temp = temp.next
                temp.next.prev = None
                temp.next = None
                self.curCap -= 1
                self.map.pop(key, None)
            node = Node(key, value)
            self.map[key] = node
            if self.head.next:
                self.head.next.setPrev(node)
            node.setPrev(self.head)
            self.curCap += 1
            return

        temp = map[key]
        temp.next.setPrev(temp.prev)
        self.head.next.setPrev(temp)
        temp.setPrev(self.head)
        temp.val = value

    def __str__(self):
        s = ""
        temp = self.head.next
        prev = self.head
        while temp:
            s += str(temp.key) + " " + str(temp.val) + "; "
            prev = prev.next
            temp = temp.next
        s += "|||"
        while prev != self.head:
            s += str(prev.key) + " " + str(prev.val) + "; "
            prev = prev.prev
        return s


lRUCache = LRUCache(2)
print(lRUCache)
lRUCache.put(1, 1)
print(lRUCache)
# 缓存是 {1=1}
lRUCache.put(2, 2)
print(lRUCache)
# 缓存是 {1=1, 2=2}
lRUCache.get(1)
print(lRUCache)
# 返回 1
lRUCache.put(3, 3)
print(lRUCache)
# 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
lRUCache.get(2)
print(lRUCache)
# 返回 -1 (未找到)
lRUCache.put(4, 4)
print(lRUCache)
# 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
lRUCache.get(1)
print(lRUCache)
# 返回 -1 (未找到)
lRUCache.get(3)
print(lRUCache)
# 返回 3
lRUCache.get(4)
print(lRUCache)
# 返回 4
