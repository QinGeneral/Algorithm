from GraphAL import UndirectedgraphAL

udgraphAL = UndirectedgraphAL(8)
print(udgraphAL)
udgraphAL.addEdge(1, 2)
udgraphAL.addEdge(1, 4)
udgraphAL.addEdge(2, 1)
udgraphAL.addEdge(2, 3)
udgraphAL.addEdge(2, 5)
udgraphAL.addEdge(3, 2)
udgraphAL.addEdge(3, 6)
udgraphAL.addEdge(4, 1)
udgraphAL.addEdge(4, 5)
udgraphAL.addEdge(5, 2)
udgraphAL.addEdge(5, 4)
udgraphAL.addEdge(5, 6)
udgraphAL.addEdge(5, 7)
udgraphAL.addEdge(6, 3)
udgraphAL.addEdge(6, 5)
udgraphAL.addEdge(6, 8)
udgraphAL.addEdge(7, 5)
udgraphAL.addEdge(7, 8)
udgraphAL.addEdge(8, 6)
udgraphAL.addEdge(8, 7)
print(udgraphAL)


def BreadthFirstSearch(s, t):
    queue = []
    queue.append(s)
    isVisited = [False] * (t - s + 1)
    road = [-1] * (t - s + 1)
    while queue:
        v = queue.pop(0)
        print(v)
        isVisited[v - 1] = True
        node = udgraphAL.data[v - 1]
        while node:
            if not isVisited[node.val - 1] and node.val not in queue:
                queue.append(node.val)
                road[node.val - 1] = v
            node = node.next
    print(road)
    result = ""
    i = t - 1
    while road[i] != -1 and i != s - 1:
        result += str(i + 1) + " "
        i = road[i] - 1
    result += str(s)
    print(" ".join(reversed(result.split())))


# BreadthFirstSearch(1, 8)

isVisited = [False] * 8
road = [-1] * 8
isFound = False


def DepthFirstSearch(s, t):
    global isFound

    if isFound:
        return
    if s == t:
        isFound = True
        return
    i = s - 1
    isVisited[i] = True
    node = udgraphAL.data[i]
    while node:
        if not isVisited[node.val - 1]:
            road[node.val - 1] = i
            DepthFirstSearch(node.val, t)
        node = node.next


s = 1
t = 7
DepthFirstSearch(s, t)
print(road)
result = ""
i = t - 1
while road[i] != -1 and i != s - 1:
    result += str(i + 1) + " "
    i = road[i]
result += str(s)
print(" ".join(reversed(result.split())))