from ListNode import ListNode


class LinkedList:
    # 守卫头结点
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head

    def insert(self, value):
        self.tail.next = ListNode(value)
        self.tail = self.tail.next

    def insertFront(self, value):
        temp = self.head.next
        self.head.next = ListNode(value)
        self.head.next.next = temp
        if self.head == self.tail:
            self.tail = self.head.next

    def remove(self, value):
        temp = self.head.next
        prev = self.head
        while temp:
            if temp.val == value:
                prev.next = temp.next
                if temp == self.tail:
                    self.tail = prev
                return temp
            temp = temp.next
            prev = prev.next

        return None
    
    def removeLast(self):
        if self.head.next == None:
            return None
        temp = self.head.next
        prev = self.head
        while temp.next:
            temp = temp.next
            prev = prev.next
        prev.next = None
        return temp

    def find(self, value):
        temp = self.head.next
        while temp:
            if temp.val == value:
                return temp
            temp = temp.next

        return None

    def __str__(self):
        result = ""
        temp = self.head.next
        while temp:
            result += str(temp.val) + "——>"
            temp = temp.next
        result += "None"
        return result


# linkedList = LinkedList()
# print(linkedList)
# linkedList.insertFront(0)
# linkedList.insert(1)
# linkedList.insert(2)
# linkedList.insert(3)
# linkedList.insert(4)
# print(linkedList)
# linkedList.remove(0)
# print(linkedList)
# linkedList.remove(2)
# print(linkedList)
# linkedList.remove(4)
# print(linkedList)
# linkedList.insertFront(0)
# print(linkedList)
# print(linkedList.removeLast().val)
# print(linkedList)
# print(linkedList.find(1).val)
# print(linkedList.find(0).val)
# print(linkedList.find(9))