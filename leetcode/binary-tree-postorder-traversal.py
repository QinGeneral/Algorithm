# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        result = []

        def postOrder(node):
            if node == None:
                return

            postOrder(node.left)
            postOrder(node.right)
            result.append(node.val)

        postOrder(root)
        return result


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        result = []
        stack = []
        map = {}
        stack.append(root)
        while stack:
            if stack[-1] in map:
                result.append(stack.pop().val)
            else:
                node = stack.pop()
                if not node.left and not node.right:
                    result.append(node.val)
                else:
                    map[node] = 1
                    stack.append(node)
                    if node.right:
                        stack.append(node.right)
                    if node.left:
                        stack.append(node.left)

        return result


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return list()

        res = list()
        stack = list()
        prev = None

        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if not root.right or root.right == prev:
                res.append(root.val)
                prev = root
                root = None
            else:
                stack.append(root)
                root = root.right

        return res
