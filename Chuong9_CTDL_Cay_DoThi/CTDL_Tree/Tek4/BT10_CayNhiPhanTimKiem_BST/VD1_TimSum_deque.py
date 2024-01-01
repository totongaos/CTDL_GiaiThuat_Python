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

class Solution:
    def rangeSumBST(self, root, low, hight):
        if not root:
            return 0
        res_sum = 0
        if low <= root.key <= hight:
            res_sum += root.key
        if low < root.key:
            res_sum += self.rangeSumBST(Solution,root.left,low,hight)
        if hight > root.key:
            res_sum += self.rangeSumBST(Solution,root.right,low,hight)
        return res_sum
#4. Ham main
if __name__ == '__main__':
    #0. input
    # n = int(input())
    # arr=[int(input()) for x in range(1,n+1)]

    #1. tao goc = A
    myTree = Tree()
    root = None

    # 2. append p.tu vao Tree
    arr = [3,2,1,5,4]
    low =2
    hight = 4

    # print("append all elements in Tree", arr)
    for i in arr:
        root = myTree.append(root, i)

    # #3. In all element in Tree
    displayTree(root, 0)

    print('sum',Solution.rangeSumBST(Solution,root,low,hight))


