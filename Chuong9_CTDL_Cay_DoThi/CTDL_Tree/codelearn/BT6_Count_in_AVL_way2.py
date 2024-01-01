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
        self.height = 1

#2. class Tree
class Tree(object):
    #1. Ham append
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

        #step 2 - update the height of the ancestor node
        node.height = 1 + max(self.get_height(node.left),
                              self.get_height(node.right))

        # Step 3 - Get the balance factor
        balance = self.get_balance(node)
        # step 4 - if the node is unbalanced, then try out the 4 cases
        # case 1:
        if balance > 1 and key < node.left.key:
            return self.right_rotate(node)

        # Case 2 - Right Right
        if balance < -1 and key > root.right.key:
            return self.left_rotate(node)

        # Case 3 - Left Right
        if balance > 1 and key > node.left.key:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        # Case 4 - Right Left
        if balance < -1 and key < node.right.key:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node
    # 1.7 Update AVL Tree
    # def update_AVL_tree(self, node):
    #     while abs(self.get_balance(node)) > 1:
    #
    #         if self.get_height(node.left) > self.get_height(node.right):
    #             p = node.left
    #             if self.get_height(p.left) >= self.get_height(p.right):
    #                 self.root = self.right_rotate(node)
    #             else:
    #                 node.left = self.left_rotate(node.left)
    #                 self.root = self.right_rotate(node)
    #         else:
    #
    #             p = node.right
    #             if self.get_height(p.right) >= self.get_height(p.left):
    #                 self.root = self.left_rotate(node)
    #             else:
    #                 node.right = self.right_rotate(node.right)
    #                 self.root = self.left_rotate(node)
    #
    #     if node.left != None:
    #         node.left = self.update_AVL_tree(node.left)
    #     if node.right != None:
    #         node.right = self.update_AVL_tree(node.right)
    #     return node

    #4. Ham turn Left
    def right_rotate(self,a):
        b = a.left
        T3 = b.right
        # Perform rotation
        b.right = a
        a.left = T3
        # Update heights
        a.height = 1 + max(self.get_height(a.left),
                           self.get_height(a.right))
        b.height = 1 + max(self.get_height(b.left),
                           self.get_height(b.right))
        # Return the new root
        return b

    #4. Ham turn Left
    def left_rotate(self,z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.get_height(z.left),
                           self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left),
                           self.get_height(y.right))
        return y

    #3. Ham get balance
    def get_balance(self,root):
        if not root: return 0
        return self.get_height(root.left) - self.get_height(root.right)
        # -1 là cây lệch trái
        # 0 là cây cân bằng
        # 1 là cây lệch bên phải của node đó.

    #2. Ham get height
    def get_height(self,root):
        if not root:     return 0
        return root.height

    # 1.5.HAm check_Avl
    def check_Avl(self, t):
        if t == None: return True
        if abs(self.get_balance(t)) > 1:   return False
        return self.check_Avl(t.left) and self.check_Avl(t.right)

    def count(self, node, x):
        if node == None:
            return 0

        if node.key == x:
            return 1 + self.count(node.left, x) + self.count(node.right, x)
        else:
            if node.key < x:
                return self.count(node.right, x)
        return self.count(node.left, x)


#1.3. Ham In all element in Tree
def displayTree(node, level):
    if not node: return
    displayTree(node.right , level + 1)
    for i in range(0, level): print("\t", end="")
    print(node.key)
    displayTree(node.left, level + 1)
    # print(level)

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

    x = 2
    # print("append all elements in Tree", arr)
    for i in arr:
        root = myTree.append(root, i)
        # root = myTree.insert_node(root,i)
    #7. Update AVL Tree
    # while abs(myTree.get_balance(myTree.root)) > 1:
    #     myTree.update_AVL_tree(myTree.root)

    # #3. In all element in Tree

    # myTree.update_AVL_tree(myTree.root)
    displayTree(root, 0)
    # count
    print("count: ", myTree.count(root, x))
    # print('get_height',myTree.get_height(root))
    #
    print("check_Avl: ", myTree.check_Avl(root))


