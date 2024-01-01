#1. class BinaryTree
class BinaryTree:
    #1.1 Khoi tao treenode
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None
    #1.2 Ham append
    def append(self, x):
        if self.val: #exist
            if x < self.val: # if given value smaller than existed node
                if self.left is None:
                    self.left = BinaryTree(x)
                else:
                    self.left.append(x)
            else: # if given value larger than existed node
                if self.right is None:
                    self.right = BinaryTree(x)
                else:
                    self.right.append(x)
        else:  # not exist yet
            self.val = x

    #1.3 Duyet trung thu tu
    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.val, end=" ")
            self.inorder(root.right)
        return "Done"

    #1.4 Duyet tien thu tu
    def preoder(self,root):
        if root:
            print(root.val, end=" ")
            self.inorder(root.left)
            self.inorder(root.right)
        return "Done"

    #1.5 Duyet hau thu tu
    def postoder(self,root):
        if root:
            self.inorder(root.left)
            self.inorder(root.right)
            print(root.val, end=" ")
        return "Done"

#2. Ham In all element in Tree
def displayTree(node, level):
    if node == None:
        return
    displayTree(node.right , level + 1)
    for i in range(0, level): print("\t", end="")
    print(node.val)
    displayTree(node.left, level + 1)

#3. Ham main
if __name__ == '__main__':
    #0. input
    # n = int(input())
    # arr=[int(input()) for x in range(1,n+1)]

    #1. tao goc = A
    root = BinaryTree()

    # 2. append p.tu vao Tree
    arr = [3,2,1,5,4]
    print("append all elements in Tree", arr)
    for i in arr:
        root.append(i)

    #3. In all element in Tree
    displayTree(root, 0)

    #3. Duyet Trung Thu Tu
    print("In-order Traversal: ",end="")
    root.inorder(root)
    print("", end="\n")
    #4. Duyet Trung Thu Tu
    print("Pre-order Traversal: ", end="")
    root.preoder(root)
    print("", end="\n")
    #5. Duyet Hau Thu Tu
    print("Pre-order Traversal: ", end="")
    root.postoder(root)
    print("", end="\n")

