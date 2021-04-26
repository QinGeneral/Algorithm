from BinaryTreeNode import BinaryTreeNode

rootNode = BinaryTreeNode(5)
rootNode.left = BinaryTreeNode(3)
rootNode.right = BinaryTreeNode(8)
rootNode.left.left = BinaryTreeNode(2)
rootNode.left.right = BinaryTreeNode(4)
rootNode.right.left = BinaryTreeNode(6)
rootNode.right.right = BinaryTreeNode(9)

def binarySearchTree(node: BinaryTreeNode, target: int):
    p = node
    while p is not None:
        if target == p.val:
            return p
        elif target > p.val:
            p = p.right
        else:
            p = p.left
    
    return None

print(binarySearchTree(rootNode, 6).val)