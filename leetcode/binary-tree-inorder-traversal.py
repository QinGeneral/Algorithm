# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        result = []

        def inOrder(node):
            if node == None:
                return

            inOrder(node.left)
            result.append(node.val)
            inOrder(node.right)

        inOrder(root)
        return result


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
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
                    if node.right:
                        stack.append(node.right)
                    stack.append(node)
                    if node.left:
                        stack.append(node.left)

        return result


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        result = []
        stack = []
        temp = root
        while stack or temp:
            while temp:
                stack.append(temp)
                temp = temp.left

            temp = stack.pop()
            result.append(temp.val)
            temp = temp.right

        return result