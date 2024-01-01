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
    def rightSideView(self, root):

        if not root:
            return []
        res = []

        queue = deque([root]) #push goc vào queue
        while queue:

            curr_len = len(queue)
            # print(curr_len)
            res.append(queue[-1].val) # this is the rightmost node for the current level
            for _ in range(curr_len):
                node = queue.popleft()
                # print(node.val)
                if node.left:
                    queue.append(node.left)
                    print(node.left.val)
                if node.right:
                    queue.append(node.right)
                    print(node.right.val)
        return res

if __name__ == '__main__':
    myTree = Tree()
    root = None
    # 2. append p.tu vao Tree
    arr = [3,2,1,5,4]

    # print("append all elements in Tree", arr)
    for i in arr:
        root = myTree.append(root, i)
    print(Solution.rightSideView(Solution,root))