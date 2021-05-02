class GraphNode:
    def __init__(self, val, weiget=1):
        self.val = val
        self.next = None
        self.weight = weiget

    def __str__(self):
        return str(self.val) + " : " + str(self.weight)
