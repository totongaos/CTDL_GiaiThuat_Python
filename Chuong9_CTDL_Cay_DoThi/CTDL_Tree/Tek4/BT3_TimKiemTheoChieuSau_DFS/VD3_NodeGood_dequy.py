'''
Cho cây nhị phân root. Tìm số nút tốt (good).
Một nút là tốt nếu như trong đường đi từ gốc tới nút đó không có nút nào lớn hơn nó.
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
    def count_good_node(self,root,maxSoFar):
        if root == None:
            return 0

        left_check = self.count_good_node(self,root.left, max(maxSoFar, root.val))
        right_check = self.count_good_node(self,root.right, max(maxSoFar, root.val))
        ans = left_check + right_check

        if root.val >= maxSoFar:
            ans += 1

        return ans


#3. Ham main
if __name__ == '__main__':
    #0. input
    # n = int(input())
    # arr=[int(input()) for x in range(1,n+1)]

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
    print("count_good_node: ",Solution.count_good_node(Solution,root, float("-inf")))

