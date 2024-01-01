'''
Tổ tiên chung thấp nhất (LCA) của cây nhị phân
Cho cây nhị phân root và 2 nút p và q trong cây. Trả về tổ tiên chung thấp nhất của p và q. Biết:

Tổ tiên chung của 2 nút p và q là nút có p và q là hậu duệ (con cháu).
Một nút là hậu duệ của chính nó.
'''


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


#2. Ham In all element in Tree
def displayTree(node, level):
    if node == None:
        return
    displayTree(node.right , level + 1)
    for i in range(0, level): print("\t", end="")
    print(node.val)
    displayTree(node.left, level + 1)
    # print(level)

#4.count_good_node
class Solution:
    def lowestCommonAncestor(self,root, p, q):
        if root == None:
            return None
        # first case
        if root.val == p or root.val == q:
            return root.val

        left_check = self.lowestCommonAncestor(self,root.left, p, q)
        right_check = self.lowestCommonAncestor(self,root.right, p, q)

        # second case
        if left_check and right_check:
            return root.val

        # third case
        if left_check:
            return left_check
        return right_check

#3. Ham main
if __name__ == '__main__':
    #0. input
    # n = int(input())
    # arr=[int(input()) for x in range(1,n+1)]
    p = 4
    q = 1

    #1. tao goc = A
    root = BinaryTree()

    # 2. append p.tu vao Tree
    arr = [4, 7, 2, 1, 3, 2, 5, 9]
    print("append all elements in Tree", arr)
    for i in arr:
        root.append(i)

    #3. In all element in Tree
    displayTree(root, 0)

    #4. Tổng đường đi
    print("count_good_node: ",Solution.lowestCommonAncestor(Solution,root, p, q))

