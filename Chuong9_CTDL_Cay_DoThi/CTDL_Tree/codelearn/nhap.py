class TreeNode:
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None
        self.height = 0

class MyTree:
    def insert(self, root, value):
        if not root:
            return TreeNode(value)
        elif value < root.data:
            root.left = self.insert(root.left, value)
        else:
            root.right = self.insert(root.right, value)

        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        return root

    def getHeight(self, root):
        if not root:
            return -1
        return root.height

    def deletioNode(self, root, value):
        if not root:
            return None
        elif root.data == value:
            return None
        elif value < root.data:
            root.left = self.deletioNode(root.left, value)
        else:
            root.right = self.deletioNode(root.right, value)
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        return root

    def printTree(self, root):
        if not root:
            print('NULL')
        else:
            if root.left:
                self.printTree(root.left)
                print(root.data, end=' ')
            if root.right:
                self.printTree(root.right)


lst = [1,2,3,4]
value = 2
root = None
binarytree = MyTree()
for i in lst:
    root = binarytree.insert(root, i)

root = binarytree.deletioNode(root, value)

binarytree.printTree(root)