class UnionUF:
    def __init__(self, n):
        self.roots = [0] * n
        for i in range(n):
            self.roots[i] = i

    def findRoot(self, i):
        root = i
        while root != self.roots[root]:
            root = roots[root]
        # 查找时进行路径压缩，优化后续查找
        while i != roots[i]:
            temp = roots[i]
            roots[i] = root
            i = temp
        return root

    def connected(self, p, q):
        return self.findRoot(p) == self.findRoot(q)

    def union(self, p, q):
        proot = self.findRoot(p)
        qroot = self.findRoot(q)
        roots[proot] = qroot


class UnionUF:
    def __init__(self, n):
        self.parent = self

    def find(self, x):
        if x.parent == x:
            return x
        else:
            return self.find(x.parent)

    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)
        xroot.parent = yroot