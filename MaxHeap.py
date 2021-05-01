class MaxHeap:
    def build(self, array):
        for i in range((len(array) - 1) // 2, 0, -1):
            self.moveDown(array, i)

    def pop(self, array):
        firstI = 1
        value = array[firstI]
        array[firstI] = array[-1]
        self.moveDown(array, firstI)
        array.pop()
        return value

    def moveDown(self, array, i):
        n = len(array)
        while True:
            targetI = i
            if i * 2 < n and array[targetI] < array[i * 2]:
                targetI = i * 2
            if i * 2 + 1 < n and array[targetI] < array[targetI * 2 + 1]:
                targetI = i * 2 + 1
            if targetI == i:
                break
            self.swap(array, i, targetI)
            i = targetI

    def insert(self, array, value):
        array.append(value)
        self.moveUp(array, len(array) - 1)

    def moveUp(self, array, i):
        while True:
            parentI = i // 2
            if parentI > 0 and array[parentI] < array[i]:
                self.swap(array, i, parentI)
                i = parentI
                parentI = i // 2
            else:
                break

    def swap(self, array, i, j):
        temp = array[i]
        array[i] = array[j]
        array[j] = temp