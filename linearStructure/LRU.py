from LinkedList import LinkedList
from LRUListNode import LRUListNode


class LRUByLinkedList:
    def __init__(self, capacity):
        self.curCap = 0
        self.capacity = capacity
        self.list = LinkedList()

    def visit(self, value):
        if self.list.find(value):
            node = self.list.remove(value)
            self.list.insertFront(node.val)
        else:
            if self.curCap == self.capacity:
                self.list.removeLast()
                self.curCap -= 1
            self.list.insertFront(value)
            self.curCap += 1

    def __str__(self):
        return str(self.list)


class LRUByHashMap:
    def __init__(self, capacity):
        self.data = [None] * capacity
        self.head = None
        self.tail = None
        self.capacity = capacity
        self.curCap = 0

    def getLRU(self, key):
        node = self.get(key)
        if node:
            self.remove(node)
            self.insertFront(node)
        else:
            return None

    def putLRU(self, key, value):
        node = self.get(key)
        if node:
            node.val = value
            self.remove(node)
            self.insertFront(node)
        else:
            if self.capacity == self.curCap:
                node = self.removeLast()
                self.removeKey(node.key)
                self.curCap -= 1
            node = self.put(key, value)
            self.insertFront(node)
            self.curCap += 1

    # linked list 操作

    def insertFront(self, node):
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = self.head.prev

    def remove(self, node):
        if self.tail == self.head:
            self.head = self.tail = None
            return
        if node.prev:
            node.prev.next = node.next
        else:
            node.next.prev = None
            self.head = node.next

        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev
        node.next = None
        node.prev = None

    def removeLast(self):
        if self.tail == None:
            return None
        elif self.tail == self.head:
            temp = self.head
            self.head = self.tail = None
            return temp
        else:
            temp = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            return temp

    # hash map 操作
    def put(self, key, value):
        index = key % self.capacity
        if self.data[index] is None:
            self.data[index] = LRUListNode(key, value)
            return self.data[index]
        else:
            temp = self.data[index]
            if temp.key == key:
                temp.val = value
                return temp
            while temp.hashNext:
                if temp.key == key:
                    temp.val = value
                    return temp
                temp = temp.hashNext
            temp.hashNext = LRUListNode(key, value)
            return temp.hashNext

    def get(self, key):
        index = key % self.capacity
        if self.data[index] is None:
            return None
        else:
            temp = self.data[index]
            while temp:
                if temp.key == key:
                    return temp
                temp = temp.hashNext
            return None

    def removeKey(self, key):
        index = key % self.capacity
        if self.data[index] is None:
            return False
        else:
            temp = self.data[index].hashNext
            prev = self.data[index]
            if prev.key == key:
                self.data[index] = None
            while temp:
                if temp.key == key:
                    prev.next = temp.next
                    return True
                temp = temp.hashNext
            return False

    def __str__(self):
        result = ""
        temp = self.head
        while temp:
            result += str(temp.val) + "——>"
            temp = temp.next
        result += "None"
        return result


# lruByLinkedList = LRUByLinkedList(3)
# lruByLinkedList.visit(0)
# print(lruByLinkedList)
# lruByLinkedList.visit(1)
# print(lruByLinkedList)
# lruByLinkedList.visit(2)
# print(lruByLinkedList)
# lruByLinkedList.visit(3)
# print(lruByLinkedList)
# lruByLinkedList.visit(4)
# print(lruByLinkedList)
# lruByLinkedList.visit(2)
# print(lruByLinkedList)
# lruByLinkedList.visit(4)
# print(lruByLinkedList)
# lruByLinkedList.visit(4)
# print(lruByLinkedList)

lruByHashMap = LRUByHashMap(3)
lruByHashMap.putLRU(0, 0)
print(lruByHashMap)
lruByHashMap.putLRU(1, 1)
print(lruByHashMap)
lruByHashMap.putLRU(2, 2)
print(lruByHashMap)
lruByHashMap.putLRU(3, 3)
print(lruByHashMap)
lruByHashMap.putLRU(4, 4)
print(lruByHashMap)
lruByHashMap.getLRU(2)
print(lruByHashMap)
lruByHashMap.getLRU(4)
print(lruByHashMap)
lruByHashMap.getLRU(4)
print(lruByHashMap)