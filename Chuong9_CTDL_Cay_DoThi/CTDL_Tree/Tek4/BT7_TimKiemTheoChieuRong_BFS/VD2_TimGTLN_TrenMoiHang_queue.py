from collections import deque

# 1. class TreeNode
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

#2. class Tree
class Tree(object):
    #2.1. Ham append
    def append(self, node, key):
        #step 1 - perform normal BST
        if not node:
            return TreeNode(key)

        elif key < node.val:
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

class Solution:
    def largestValues(self, root):

        if not root:
            return []
        res = []

        queue = deque([root]) #push goc vào queue
        while queue:
            curr_max = float("-inf") # this will store the largest value for the current level
            curr_len = len(queue)

            for _ in range(curr_len):
                node = queue.popleft()
                curr_max = max(curr_max,node.val)
                # print(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(curr_max)
        return res

if __name__ == '__main__':
    myTree = Tree()
    root = None
    # 2. append p.tu vao Tree
    arr = [5,3,6,7,11,4,15,8,0,1,2]

    # print("append all elements in Tree", arr)
    for i in arr:
        root = myTree.append(root, i)
    print(Solution.largestValues(Solution,root))