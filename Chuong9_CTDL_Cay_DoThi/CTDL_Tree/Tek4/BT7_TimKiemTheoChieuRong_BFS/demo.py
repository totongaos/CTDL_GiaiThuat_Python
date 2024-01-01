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

def print_all_nodes(root):
    queue = deque([root])
    while queue:
        nodes_in_current_level = len(queue)
        # do some logic here for the current level

        for _ in range(nodes_in_current_level):

            node = queue.popleft()

            # do some logic here on the current node
            print(node.val)

            # put the next level onto the queue
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)


if __name__ == '__main__':
    myTree = Tree()
    root = None
    # 2. append p.tu vao Tree
    arr = [3,2,1,5,4]
    x = 5

    # print("append all elements in Tree", arr)
    for i in arr:
        root = myTree.append(root, i)
    print_all_nodes(root)