import sys
sys.path.append("..")
from TreeNode import TreeNode


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        self.array = []
        self.inOrder(root)
        for i in range(1, len(self.array)):
            if self.array[i] <= self.array[i - 1]:
                return False
        return True

    def inOrder(self, node: TreeNode):
        if node == None:
            return

        self.inOrder(node.left)
        self.array.append(node.val)
        self.inOrder(node.right)


class Solution2:
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(node: TreeNode, lower=float("-inf"), upper=float("inf")):
            if node is None:
                return True
            val = node.val
            if val <= lower or val >= upper:
                return False

            return helper(node.left, lower, val) and helper(node.right, val, upper)

        return helper(root)