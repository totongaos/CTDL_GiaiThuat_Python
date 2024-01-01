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
    def getMinimumDifference(self, root):
        def dsf_inoder(root):
            stack = []
            values = []
            curr = root
            if not root:
                return []
            while stack or curr:
                if curr:
                    stack.append(curr)
                    curr = curr.left
                else:
                    curr = stack.pop()
                    values.append(curr.key)
                    curr=curr.right
            return values

        values = dsf_inoder(root)
        ans = float("inf")
        for i in range(1, len(values)):
            ans = min(ans,values[i] - values[i-1])
        return ans
#4. Ham main
if __name__ == '__main__':
    #0. input
    # n = int(input())
    # arr=[int(input()) for x in range(1,n+1)]

    #1. tao goc = A
    myTree = Tree()
    root = None

    # 2. append p.tu vao Tree
    arr = [3,8,0,6,9]

    # print("append all elements in Tree", arr)
    for i in arr:
        root = myTree.append(root, i)

    # #3. In all element in Tree
    displayTree(root, 0)
    #3. In all element in Tree

    print('getMinimumDifference',Solution.getMinimumDifference(Solution,root))


