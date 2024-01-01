'''
Tao cay AVL nhị phân tìm kiếm
'''


# 1. class TreeNode
class TreeNode(object):
    # 1.1 Khoi tao treenode
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 0

#2. class Tree
class Tree(object):
    #1. Ham append
    def append(self, root, key):
        #step 1 - perform normal BST
        if not root: return TreeNode(key)
        elif key < root.val:
            root.left = self.append(root.left, key)
        else:
            root.right = self.append(root.right,key)

        #step 2 - update the height of the ancestor node
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # Step 3 - Get the balance factor
        balance = self.get_balance(root)

        #step 4 - if the node is unbalanced, then try out the 4 cases
        #case 1: LL
        if balance > 1 and key < root.left.val:
            return self.right_rotate(root)
        #case 2: RR
        if balance < -1 and key > root.right.val:
            return self.left_rotate(root)
        #case 3: LR
        if balance > 1 and key > root.left.val:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        #case 4: RL
        if balance < -1 and key < root.right.val:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
        return root

    #4. Ham turn Left
    def right_rotate(self,a):
        b = a.left
        d = b.right
        # Perform rotation
        b.right = a
        a.left = d
        # Update heights
        a.height = 1 + max(self.get_height(a.left), self.get_height(a.right))
        b.height = 1 + max(self.get_height(b.left), self.get_height(b.right))
        # Return the new root
        return b

    #4. Ham turn Left
    def left_rotate(self,a):
        b = a.right
        d = b.left
        # Perform rotation
        b.left = a
        a.right = d
        # Update heights
        a.height = 1 + max(self.get_height(a.left), self.get_height(a.right))
        b.height = 1 + max(self.get_height(b.left), self.get_height(b.right))
        # Return the new root
        return b

    #3. Ham get balance
    def get_balance(self,root):
        if not root: return 0
        return self.get_height(root.left) - self.get_height(root.right)
        # -1 là cây lệch trái
        # 0 là cây cân bằng
        # 1 là cây lệch bên phải của node đó.

    #2. Ham get height
    def get_height(self,root):
        if not root:
            return -1
        return root.height

    # 1.5.HAm check_Avl
    def check_Avl(self, t):
        if t == None: return True
        if abs(self.get_balance(t)) > 1:
            return False
        return self.check_Avl(t.left) and self.check_Avl(t.right)

#1.3. Ham In all element in Tree
def displayTree(node, level):
    if not node: return
    displayTree(node.right , level + 1)
    for i in range(0, level): print("\t", end="")
    print(node.val)
    displayTree(node.left, level + 1)
    # print(level)

#3. Ham main
if __name__ == '__main__':
    #0. input
    # n = int(input())
    # arr=[int(input()) for x in range(1,n+1)]

    #1. tao goc = A
    myTree = Tree()
    root = None

    # 2. append p.tu vao Tree
    arr = [1, 2, 3, 1, 2, 2, 2]
    print("append all elements in Tree", arr)
    for i in arr:
        root = myTree.append(root, i)

    # #3. In all element in Tree
    displayTree(root,0)
    print('get_height',myTree.get_height(root))
    print(myTree.check_Avl(root))

    # displayTree(a, 0)
    # print(myTree.check_Avl(a))