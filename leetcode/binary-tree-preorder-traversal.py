# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        result = []

        def inOrder(node):
            if node == None:
                return

            result.append(node.val)
            inOrder(node.left)
            inOrder(node.right)

        inOrder(root)
        return result


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        result = []
        stack = []
        temp = root
        stack.append(root)
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return result

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        result = []
        stack = []
        temp = root
        while stack or temp:
            while temp:
                result.append(temp.val)
                stack.append(temp)
                temp = temp.left
            
            temp = stack.pop()
            temp = temp.right

        return result