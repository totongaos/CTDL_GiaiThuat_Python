#1. Khai báo node của cây
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

#2. Ham In all element in Tree
def displayTree(node, level):
    if node == None:
        return
    displayTree(node.right , level + 1)
    for i in range(0, level): print("\t", end="")
    print(node.val)
    displayTree(node.left, level + 1)


if __name__ == '__main__':
    #1. tao goc = A
    root = TreeNode('A')

    #2. insert cac ptu cua Tree
    root.left = TreeNode("A-L")
    root.right = TreeNode("A-R")
    root.left.right = TreeNode("A-L-R")
    root.left.left = TreeNode("A-L-l")
    root.right.left = TreeNode("A-R-L")
    root.right.right = TreeNode("A-R-r")

    #3. In all element in Tree
    displayTree(root,0)