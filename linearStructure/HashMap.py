from ListNode import ListNode

class HashMap:
    def __init__(self, capacity):
        self.data = [None] * capacity
        self.capacity = capacity

    def put(self, key, value):
        index = key % self.capacity
        if self.data[index] is None:
            self.data[index] = ListNode(value)
            self.data[index].setKey(key)
        else:
            temp = self.data[index]
            if temp.key == key:
                temp.val = value
                return
            while temp.next:
                if temp.key == key:
                    temp.val = value
                    return
                temp = temp.next
            temp.next = ListNode(value)
            temp.next.setKey(key)
    
    def get(self, key):
        index = key % self.capacity
        if self.data[index] is None:
            return -1
        else:
            temp = self.data[index]
            while temp:
                if temp.key == key:
                    return temp.val
                temp = temp.next
            return -1

hashMap = HashMap(3)
hashMap.put(0, 'b')
print(hashMap.get(0))
hashMap.put(0, 'a')
print(hashMap.get(0))
hashMap.put(3, 'c')
print(hashMap.get(3))
