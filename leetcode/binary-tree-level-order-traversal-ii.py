class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue = []
        queue.append(root)
        result = []
        while queue:
            size = len(queue)
            r = []
            while True:
                if size == 0:
                    break
                temp = queue.pop(0)
                size -= 1
                r.append(temp.val)
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
            result.append(r)
        result.reverse()
        return result