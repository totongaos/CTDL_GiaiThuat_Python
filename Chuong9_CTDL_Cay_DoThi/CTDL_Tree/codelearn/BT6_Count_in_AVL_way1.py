'''
Hãy biến đổi cây đó thành cây AVL. Nhập vào một số nguyên x, hãy đếm số lượng phần tử có giá trị bằng x trong cây đó.

'''


#1. class BinaryTree
class Tree:
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
                    self.left = Tree(x)
                else:
                    self.left.append(x)
            else: # if given value larger than existed node
                if self.right is None:
                    self.right = Tree(x)
                else:
                    self.right.append(x)
            return self.val
        else:  # not exist yet
            self.val = x
            return self.val

    #1.6 Turn Right
    def turn_r(self, a):
        b = a.left
        d = b.right
        b.right = a
        a.left = d

        return b
    #1.6 Turn left
    def turn_l(self, a):
        y = a.right
        c = y.left
        y.left = a
        a.right = c

        return y

    #1.7 Update AVL Tree
    def update_AVL_tree(self, root):
        while abs(maxDept(root.left) - maxDept(root.right)) > 1:
            if maxDept(root.left) > maxDept(root.right):
                p = root.left
                if maxDept(p.left) >= maxDept(p.right):
                    root = self.turn_r(root)
                else:
                    root.left = self.turn_l(root.left)
                    root = self.turn_r(root)
            else:
                p = root.right
                if maxDept(p.right) >= maxDept(p.left):
                    root = self.turn_l(root)
                else:
                    root.right = self.turn_r(root.right)
                    root = self.turn_l(root)

        if root.left != None:
            root.left = self.update_AVL_tree(root.left)
        if root.right != None:
            root.right = self.update_AVL_tree(root.right)
        return root

#1.3. Ham In all element in Tree
def displayTree(node, level):
    if not node: return
    displayTree(node.right , level + 1)
    for i in range(0, level): print("\t", end="")
    print(node.val)
    displayTree(node.left, level + 1)
    # print(level)

#1.4. Ham maxDept
def maxDept(t):
    if t == None: return -1
    return 1 + max(maxDept(t.left), maxDept(t.right))

#1.5.HAm check_Avl
def check_Avl(t):
    if t == None: return True
    if abs(maxDept(t.left) - maxDept(t.right)) > 1:
        return False
    return check_Avl(t.left) and check_Avl(t.right)

def count(node, x):
    if node == None:
        return 0

    if node.val == x:
        return 1 + count(node.left, x) + count(node.right, x)
    else:
        if node.val < x:
            return count(node.right, x)
    return count(node.left, x)

#3. Ham main
if __name__ == '__main__':
    #0. input
    # n = int(input())
    # arr=[int(input()) for x in range(1,n+1)]
    # x = int(input())

    #1. tao goc = A

    myTree = Tree()
    root = None

    # 2. append p.tu vao Tree
    arr = [5,3,6,7,11,4,15,8,0,1,2]
    x =5
    print("append all elements in Tree", arr)
    for i in arr:
        root = myTree.append(i)

    #7. Update AVL Tree
    if check_Avl(myTree) == False:
        root = myTree.update_AVL_tree(myTree)


    # 3. In all element in Tree
    displayTree(root, 0)

    # count
    print("count: ", count(root, x))
