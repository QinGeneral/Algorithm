from BinaryTreeNode import BinaryTreeNode

rootNode = BinaryTreeNode(1)
rootNode.left = BinaryTreeNode(2)
rootNode.right = BinaryTreeNode(3)
rootNode.left.left = BinaryTreeNode(4)
rootNode.left.right = BinaryTreeNode(5)
rootNode.right.left = BinaryTreeNode(6)
rootNode.right.right = BinaryTreeNode(7)
rootNode.right.left.right = BinaryTreeNode(8)
rootNode.right.right.left = BinaryTreeNode(9)


def preOrder(node: BinaryTreeNode):
    if node == None:
        return

    print(node.val)
    preOrder(node.left)
    preOrder(node.right)


def inOrder(node: BinaryTreeNode):
    if node == None:
        return

    inOrder(node.left)
    print(node.val)
    inOrder(node.right)


def postOrder(node: BinaryTreeNode):
    if node == None:
        return

    postOrder(node.left)
    postOrder(node.right)
    print(node.val)


def printNode(node: BinaryTreeNode):
    if node == None:
        return

    print(node.val)


preOrder(rootNode)
print("---------------")
inOrder(rootNode)
print("---------------")
postOrder(rootNode)
print("---------------")
printNode(rootNode)
levelOrder(rootNode)