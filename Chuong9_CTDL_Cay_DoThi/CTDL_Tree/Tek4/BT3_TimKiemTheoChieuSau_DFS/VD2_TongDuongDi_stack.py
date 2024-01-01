'''
Tổng đường đi. Cho cây nhị phân root và số nguyên targetSum.

Trả về true nếu tồn tại đường đi từ một lá nào đó đến gốc sao cho tổng giá trị các nút trên đường đi là targetSum.
Ngược lại, trả về false.
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

#4.sum_node
class Solution:
    def sum_node(self,root,targetSum):
        if root == None:
            return False
        stack = [(root, 0)]

        while stack:
            node , curr = stack.pop()
            # if both children are null, then the node is a leaf
            if node.right == None and node.right == None:
                if curr + node.val == targetSum:
                    return True

            curr+= node.val

            if node.left:
                stack.append((node.left,curr))
            if node.right:
                stack.append((node.right,curr))
        return False



#3. Ham main
if __name__ == '__main__':
    #0. input
    # n = int(input())
    # arr=[int(input()) for x in range(1,n+1)]
    targetSum = 21

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
    print("sum_node: ",Solution.sum_node(Solution,root, targetSum))

