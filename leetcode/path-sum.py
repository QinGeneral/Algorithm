class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if root is None:
            return False
        if root.left == None and root.right == None:
            return targetSum == root.val

        if root.left and self.hasPathSum(root.left, targetSum - root.val):
            return True
        if root.right and self.hasPathSum(root.right, targetSum - root.val):
            return True
        
        return False