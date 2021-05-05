# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        map = {}
        def preOrder(node, column, row):
            if not node:
                return
            if column not in map:
                map[column] = {}
            if row not in map[column]:
                map[column][row] = []
            map[column][row].append(node.val)
            preOrder(node.left, column - 1, row + 1)
            preOrder(node.right, column + 1, row + 1)
        preOrder(root, 0, 0)
            
        result = []
        for i in sorted(map.keys()):
            r = []
            for j in sorted(map[i].keys()):
                r += map[i][j]
            result.append(r)

        return result