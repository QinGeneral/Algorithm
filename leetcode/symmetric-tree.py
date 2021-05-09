# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        queue = []
        queue.append(root)
        while queue:
            size = len(queue)
            val = []
            while size > 0:
                node = queue.pop(0)
                if node is None:
                    val.append(None)
                else:
                    val.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
                size -= 1

            if not self.isSym(val):
                return False
        return True

    def isSym(self, array):
        i = 0
        j = len(array) - 1
        while i < j:
            if array[i] != array[j]:
                return False
            i += 1
            j -= 1
        return True


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        def dfs(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            if left.val != right.val:
                return False
            return dfs(left.left, right.right) and dfs(left.right, right.left)
        return dfs(root.left, root.right)
