'''
Hãy kiểm tra xem cây đó có phải là câu AVL nhị phân tìm kiếm hay không
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
        else:  # not exist yet
            self.val = x

    #1.3. Ham In all element in Tree
    def displayTree(self,node, level):
        if node == None:
            return
        self.displayTree(node.right , level + 1)
        for i in range(0, level): print("\t", end="")
        print(node.val)
        self.displayTree(node.left, level + 1)
        # print(level)

    #1.4. Ham maxDept
    def maxDept(self,root):
        if root == None:
            return -1

        return max(self.maxDept(root.left), self.maxDept(root.right)) + 1

    #1.5.HAm check_Avl
    def check_Avl(self, root):
        if root == None:
            return True
        if abs(self.maxDept(root.right) - self.maxDept(root.left)) > 1:
            return False
        return self.check_Avl(root.left) or self.check_Avl(root.right)



#3. Ham main
if __name__ == '__main__':
    #0. input
    # n = int(input())
    # arr=[int(input()) for x in range(1,n+1)]

    #1. tao goc = A
    root = Tree()

    # 2. append p.tu vao Tree
    arr = [4, 7, 2, 1, 3, 2, 5]
    print("append all elements in Tree", arr)
    for i in arr:
        root.append(i)

    #3. In all element in Tree
    root.displayTree(root,0)

    #4. maxDept
    print("maxDept: ",root.maxDept(root))

    #5. check_Avl
    print("check_Avl: ",root.check_Avl(root))

