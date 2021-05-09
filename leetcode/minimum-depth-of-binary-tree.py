# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0

        queue = []
        queue.append(root)
        minDepth = 0
        while queue:
            sz = len(queue)
            minDepth += 1
            while sz > 0:
                temp = queue.pop(0)
                if not temp.left and not temp.right:
                    return minDepth
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
                sz -= 1
        return minDepth


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        def dfs(root, level):
            if not root:
                return level
            if root.left and root.right:
                return 1 + min(dfs(root.left, level), dfs(root.right, level))
            elif root.left:
                return 1 + dfs(root.left, level)
            elif root.right:
                return 1 + dfs(root.right, level)
            else:
                return level + 1

        maxDepth = dfs(root, 0)
        return maxDepth