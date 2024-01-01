#1. Khai báo node của cây
class AVL_Tree:
    # 1.1 Khoi tao AVL_Tree
    def __init__(self, val=None, height = 0):
        self.height = height
        self.val = val
        self.left = None
        self.right = None
