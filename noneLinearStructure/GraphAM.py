# AdjacencyMatrix 邻接矩阵
# AdjacencyList 邻接表

class DirectedGraphAM:
    def __init__(self, dime):
        self.data = [[0 for i in range(dime)] for j in range(dime)]

    def addEdge(self, i, j):
        self.data[i - 1][j - 1] = 1

    def hasEdge(self, i, j):
        return self.data[i - 1][j - 1] == 1

    def __str__(self):
        finalR = ""
        for i in range(len(self.data)):
            result = ""
            for j in self.data[i]:
                result += str(j) + " "
            finalR += result + "\n"
        return finalR

dgraphAM = DirectedGraphAM(4)
print(dgraphAM)
dgraphAM.addEdge(1, 2)
dgraphAM.addEdge(2, 3)
dgraphAM.addEdge(3, 1)
dgraphAM.addEdge(3, 2)
dgraphAM.addEdge(4, 2)
dgraphAM.addEdge(4, 3)
print(dgraphAM)

class UndirectedGraphAM:
    def __init__(self, dime):
        self.data = [[0 for i in range(dime)] for j in range(dime)]

    def addEdge(self, i, j):
        self.data[i - 1][j - 1] = 1
        self.data[j - 1][i - 1] = 1

    def hasEdge(self, i, j):
        return self.data[i - 1][j - 1] == 1

    def __str__(self):
        finalR = ""
        for i in range(len(self.data)):
            result = ""
            for j in self.data[i]:
                result += str(j) + " "
            finalR += result + "\n"
        return finalR


# ugraphAM = UndirectedGraphAM(4)
# print(ugraphAM)
# ugraphAM.addEdge(1, 2)
# ugraphAM.addEdge(1, 3)
# ugraphAM.addEdge(2, 3)
# ugraphAM.addEdge(2, 4)
# ugraphAM.addEdge(3, 4)
# print(ugraphAM)

class WeightedUndirectedGraph:
    def __init__(self, dime):
        self.data = [[0 for i in range(dime)] for j in range(dime)]

    def addEdge(self, i, j, weiget):
        self.data[i - 1][j - 1] = weiget
        self.data[j - 1][i - 1] = weiget

    def hasEdge(self, i, j):
        return self.data[i - 1][j - 1] > 0

    def __str__(self):
        finalR = ""
        for i in range(len(self.data)):
            result = ""
            for j in self.data[i]:
                result += str(j) + " "
            finalR += result + "\n"
        return finalR

wugraphAM = WeightedUndirectedGraph(4)
wugraphAM.addEdge(1, 2, 5)
wugraphAM.addEdge(1, 3, 3)
wugraphAM.addEdge(2, 3, 2)
wugraphAM.addEdge(2, 4, 6)
wugraphAM.addEdge(3, 4, 1)
print(wugraphAM)