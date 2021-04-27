from BinaryTreeNode import BinaryTreeNode
from tree import inOrder

rootNode = BinaryTreeNode(5)
# rootNode.left = BinaryTreeNode(3)
# rootNode.right = BinaryTreeNode(8)
# rootNode.left.left = BinaryTreeNode(2)
# rootNode.left.right = BinaryTreeNode(4)
# rootNode.right.left = BinaryTreeNode(6)
# rootNode.right.right = BinaryTreeNode(9)


def calculateChildNum(node: BinaryTreeNode):
    if node is None:
        print("node is None")
        return 0

    node.childNum = calculateChildNum(node.left) + calculateChildNum(node.right) + 1
    return node.childNum


def findMaxKValue(node: BinaryTreeNode, k: int):
    if node is None:
        print("k not find, node is None")
        return

    rightChildCount = 0
    if node.right is not None:
        rightChildCount = node.right.childNum
    if k == rightChildCount + 1:
        return node
    elif k > rightChildCount + 1:
        return findMaxKValue(node.left, k - rightChildCount - 1)
    else:
        return findMaxKValue(node.right, k)


def insert(node: BinaryTreeNode, value: int):
    if node is None:
        print("node is None")
        return

    if value >= node.val:
        if node.right is None:
            newNode = BinaryTreeNode(value)
            node.right = newNode
            newNode.parent = node
        else:
            insert(node.right, value)
    else:
        if node.left is None:
            newNode = BinaryTreeNode(value)
            node.left = newNode
            newNode.parent = node
        else:
            insert(node.left, value)


def delete(node: BinaryTreeNode, value: int):
    if node is None:
        print(str(value) + " is not in the tree")
        return

    if value == node.val:
        if node.left is None and node.right is None:
            if node.parent.left == node:
                node.parent.left = None
            else:
                node.parent.right = None
        elif node.right is None:
            node.left.parent = node.parent
            node.parent.left = node.left
        else:
            leftNode = node.right
            while leftNode is not None and leftNode.left is not None:
                leftNode = leftNode.left
            if leftNode != node.right:
                leftNode.parent.left = None
                leftNode.right = node.right

            leftNode.parent = node.parent
            if node.parent.left == node:
                node.parent.left = leftNode
            else:
                node.parent.right = leftNode
            leftNode.left = node.left

    elif value > node.val:
        delete(node.right, value)
    else:
        delete(node.left, value)


inOrder(rootNode)
print("---------------")
insert(rootNode, 3)
insert(rootNode, 8)
insert(rootNode, 2)
insert(rootNode, 4)
insert(rootNode, 6)
insert(rootNode, 9)
insert(rootNode, 8.5)
insert(rootNode, 10)
calculateChildNum(rootNode)
inOrder(rootNode)
print("---------------")
for i in range(1, 10):
    node = findMaxKValue(rootNode, i)
    print(node.val, node.childNum)
# delete(rootNode, 1)
# inOrder(rootNode)
# print("---------------")
# delete(rootNode, 4)
# inOrder(rootNode)
# print("---------------")
# delete(rootNode, 3)
# inOrder(rootNode)
# print("---------------")
# delete(rootNode, 8)
# inOrder(rootNode)
# print("---------------")


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


# print(binarySearchTree(rootNode, 6).val)