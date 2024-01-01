'''
Cho một dãy n số nguyên. Hãy cài đặt các số trong dãy đó vào kiểu dữ liệu cây.
In cây theo cách duyệt trung thứ tự (xem lý thuyết).
Sau mỗi phần tử có đúng một khoảng trắng.


- Duyệt tiền thứ tự (Pre-order Traversal)
- Duyệt trung thứ tự (In-order Traversal)
- Duyệt hậu thứ tự (Post-order Traversal)
'''


#1. class BinaryTree
class BinaryTree:
    #1.1 Khoi tao treenode
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None
    #1.2 Ham insert
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

#2. Ham main
if __name__ == '__main__':
    #0. input
    # n = int(input())
    # arr=[int(input()) for x in range(1,n+1)]

    #1. tao goc = A
    root = BinaryTree()

    # 2. Insert p.tu vao Tree
    arr = [3,2,1,5,4]
    for i in arr:
        root.append(i)

    #3. In all element in Tree
    root.inorder(root)


