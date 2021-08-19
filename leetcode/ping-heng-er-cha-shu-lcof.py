# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True

        depthArray = []
        self.maxValue = 0
        self.minValue = float("-inf")

        def getDepth(node, depth):
            if not node:
                return
            if not node.left and not node.right:
                self.maxValue = max(self.maxValue, depth)
                self.minValue = min(self.minValue, depth)
                return
            getDepth(node.left, depth + 1)
            getDepth(node.right, depth + 1)

        getDepth(root, 1)
        return self.maxValue > self.minValue - 1


print(Solution().isBalanced())