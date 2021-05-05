class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def helper(root, p, q):
            if not root:
                return None
            if root == p or root == q:
                return root
            nl = helper(root.left, p, q)
            nr = helper(root.right, p, q)
            if nl and nr:
                return root
            elif nl:
                return nl
            elif nr:
                return nr
            else:
                return None
        return helper(root, p, q)