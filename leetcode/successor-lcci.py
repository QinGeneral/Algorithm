# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        self.queue = []
        self.inOrder(root)
        for i in range(len(self.queue)):
            if self.queue[i] == p:
                break
        if i == len(self.queue) - 1:
            return None
        else:
            return self.queue[i + 1]
    
    def inOrder(self, node: TreeNode):
        if node == None:
            return

        self.inOrder(node.left)
        self.queue.append(node)
        self.inOrder(node.right)

class Solution2:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        if root is None:
            return None
        
        if p.val >= root.val:
            return self.inorderSuccessor(root.right, p)
        else:
            node = self.inorderSuccessor(root.left, p)
            if node:
                return node
            else:
                return root