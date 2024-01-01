'''
Tao cay AVL nhị phân tìm kiếm
Hãy biến đổi cây đó thành cây AVL. Nhập vào một số nguyên x, hãy đếm số lượng phần tử có giá trị bằng x trong cây đó.
'''


# 1. class TreeNode
class TreeNode(object):
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

#2. class Tree
class Tree(object):
    #2.1. Ham append
    def append(self, node, key):
        #step 1 - perform normal BST
        if not node:
            return TreeNode(key)

        elif key < node.key:
            if node.left is None:
                node.left = TreeNode(key)
            else:
                node.left = self.append(node.left, key)
        else:
            if node.right is None:
                node.right = TreeNode(key)
            else:
                node.right = self.append(node.right,key)

        return node

    #HAM 2.2 deleteValue
    def deleteValue(self, root, value):
        if root:
            if root.key == value:
                root = None
            elif value < root.key:
                root.left = self.deleteValue(root.left, value)
            else:
                root.right = self.deleteValue(root.right, value)
        return root

    #2.3 Duyet trung thu tu
    def inorder(self,root):
        if not root :
            return
        elif root.key != None:
            self.inorder(root.left)
            print(root.key, end=" ")
            self.inorder(root.right)
        return "Done"

#3. Ham In all element in Tree
def displayTree(node, level):
    if not node:
        return
    elif node.key != None:
        displayTree(node.right , level + 1)
        for i in range(0, level): print("\t", end="")
        print(node.key)
        displayTree(node.left, level + 1)
        # print(level)

#4. Ham main
if __name__ == '__main__':
    #0. input
    # n = int(input())
    # arr=[int(input()) for x in range(1,n+1)]
    # x = int(input())

    #1. tao goc = A
    myTree = Tree()
    root = None

    # 2. append p.tu vao Tree
    arr = [3,2,1,5,4]
    x = 5

    # print("append all elements in Tree", arr)
    for i in arr:
        root = myTree.append(root, i)

    # #3. In all element in Tree
    displayTree(root, 0)
    root = myTree.deleteValue(root, x)

    print("---------------------------")
    displayTree(root, 0)
    # 3. In all element in Tree
    if root == None:
        print("NULL")
    else:
        myTree.inorder(root)



