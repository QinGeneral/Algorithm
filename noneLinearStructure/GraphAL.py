import sys

sys.path.append("..")
from GraphNode import GraphNode

# AdjacencyMatrix 邻接矩阵
# AdjacencyList 邻接表


class DirectedGraphAL:
    def __init__(self, dime):
        self.data = [None] * dime

    def addEdge(self, i, j):
        index = i - 1
        if self.data[index]:
            temp = self.data[index]
            while temp.next:
                temp = temp.next
            temp.next = GraphNode(j)
        else:
            self.data[index] = GraphNode(j)

    def hasEdge(self, i, j):
        index = i - 1
        if self.data[index]:
            temp = self.data[index]
            while temp:
                if temp.val == j:
                    return True
                temp = temp.next
        return False

    def __str__(self):
        finalR = ""
        for i in range(len(self.data)):
            result = str(i) + ": "
            temp = self.data[i]
            while temp:
                result += str(temp.val) + "——>"
                temp = temp.next
            result += "None"
            finalR += result + "\n"
        return finalR


# dgraphAL = DirectedGraphAL(5)
# print(dgraphAL)
# dgraphAL.addEdge(1, 2)
# dgraphAL.addEdge(2, 3)
# dgraphAL.addEdge(2, 4)
# dgraphAL.addEdge(2, 5)
# dgraphAL.addEdge(4, 1)
# dgraphAL.addEdge(4, 2)
# dgraphAL.addEdge(5, 3)
# dgraphAL.addEdge(5, 4)
# print(dgraphAL)
# print(dgraphAL.hasEdge(1, 5))
# print(dgraphAL.hasEdge(1, 2))
# print(dgraphAL.hasEdge(2, 1))
# print(dgraphAL.hasEdge(5, 4))


class UndirectedgraphAL:
    def __init__(self, dime):
        self.data = [None] * dime

    def addEdgeDirectly(self, i, j):
        index = i - 1
        if self.data[index]:
            temp = self.data[index]
            if temp.val == j:
                return
            while temp.next:
                if temp.val == j:
                    return
                temp = temp.next
            if temp.val == j:
                return
            temp.next = GraphNode(j)
        else:
            self.data[index] = GraphNode(j)

    def addEdge(self, i, j):
        self.addEdgeDirectly(i, j)
        self.addEdgeDirectly(j, i)

    def hasEdge(self, i, j):
        index = i - 1
        if self.data[index]:
            temp = self.data[index]
            while temp:
                if temp.val == j:
                    return True
                temp = temp.next
        return False

    def __str__(self):
        finalR = ""
        for i in range(len(self.data)):
            result = str(i + 1) + ": "
            temp = self.data[i]
            while temp:
                result += str(temp.val) + "——>"
                temp = temp.next
            result += "None"
            finalR += result + "\n"
        return finalR


# print("--------------")
# udgraphAL = UndirectedgraphAL(5)
# print(udgraphAL)
# udgraphAL.addEdge(1, 2)
# udgraphAL.addEdge(2, 3)
# udgraphAL.addEdge(2, 4)
# udgraphAL.addEdge(2, 5)
# udgraphAL.addEdge(4, 1)
# udgraphAL.addEdge(4, 2)
# udgraphAL.addEdge(5, 3)
# udgraphAL.addEdge(5, 4)
# print(udgraphAL)
# print(udgraphAL.hasEdge(1, 5))
# print(udgraphAL.hasEdge(1, 2))
# print(udgraphAL.hasEdge(5, 4))


class WeightedUndirectedGraph:
    def __init__(self, dime):
        self.data = [None] * dime

    def addEdgeDirectly(self, i, j, weight):
        index = i - 1
        if self.data[index]:
            temp = self.data[index]
            if temp.val == j:
                return
            while temp.next:
                if temp.val == j:
                    return
                temp = temp.next
            temp.next = GraphNode(j, weight)
        else:
            self.data[index] = GraphNode(j, weight)

    def addEdge(self, i, j, weight):
        self.addEdgeDirectly(i, j, weight)
        self.addEdgeDirectly(j, i, weight)

    def hasEdge(self, i, j):
        index = i - 1
        if self.data[index]:
            temp = self.data[index]
            while temp:
                if temp.val == j:
                    return temp
                temp = temp.next
        return None

    def __str__(self):
        finalR = ""
        for i in range(len(self.data)):
            result = str(i + 1) + ": "
            temp = self.data[i]
            while temp:
                result += str(temp) + "——>"
                temp = temp.next
            result += "None"
            finalR += result + "\n"
        return finalR


# print("--------------")
# wudgraphAL = WeightedUndirectedGraph(5)
# print(wudgraphAL)
# wudgraphAL.addEdge(1, 2, 5)
# wudgraphAL.addEdge(2, 3, 2)
# wudgraphAL.addEdge(2, 4, 6)
# wudgraphAL.addEdge(2, 5, 9)
# wudgraphAL.addEdge(4, 1, 3)
# wudgraphAL.addEdge(4, 2, 6)
# wudgraphAL.addEdge(5, 3, 2)
# wudgraphAL.addEdge(5, 4, 1)
# print(wudgraphAL)
# print(wudgraphAL.hasEdge(1, 5))
# print(wudgraphAL.hasEdge(1, 2))
# print(wudgraphAL.hasEdge(5, 4))