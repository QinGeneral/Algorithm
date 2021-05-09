# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        lDepth = self.maxDepth(root.left)
        rDepth = self.maxDepth(root.right)
        return lDepth + 1 if lDepth > rDepth else rDepth + 1


class Solution2:
    def maxDepth(self, root: TreeNode) -> int:
        queue = []
        queue.append(root)
        maxDepth = 0
        while queue:
            sz = len(queue)
            while sz > 0:
                temp = queue.pop(0)
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
                sz -= 1
            maxDepth += 1
        return maxDepth


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def dfs(root, level):
            if not root:
                return level
            return max(dfs(root.left, level), dfs(root.right, level)) + 1
        maxDepth = dfs(root, 0)
        return maxDepth