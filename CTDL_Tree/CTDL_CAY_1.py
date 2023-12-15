'''
Cho một dãy n số nguyên. Hãy cài đặt các số trong dãy đó vào kiểu dữ liệu cây. In cây theo cách duyệt trung thứ tự (xem lý thuyết).
Sau mỗi phần tử có đúng một khoảng trắng.

'''

#1. class Node
class Node:
    #1. Khoi tao 1 nut moi
    def __init__(self, key=None):
        self.key = key
        self.left = None
        self.right = None

    #2. Ham insert key vao CTDL Tree
    def insert(self,key):
        if self == None: #2.1 node chua dc khoi tao
            node = Node(key)
            self = node
            return
        #2.2 node da co value ->
        if key < self.key:
            if self.left == None:
                self.left = Node(key)
            else:
                self.left.insert(key)
        elif key > self.key:
            if self.right == None:
                self.right = Node(key)
            else:
                self.right.insert(key)
        else:
            print(f'Be duplicated {key}')

#2. class TreeNode
class TreeNode:
    #1. Ham KHOI TAO
    def __init__(self, key=None):
        if key == None:
            self.root = None
        else:
            self.root = Node(key) #tao node dau tien cho tree

    #2. HAM INSERT
    def inser(self, key):
        if self.root == None:
            self.root = Node(key)
            print(f'Done inser {key}')
        else:
            self.root.insert(key)
            print(f'Done inser {key}')

    #3. Ham  DISPLAY: LNR
    def display_L_node_R(self, root = 0):
        node_curr = root
        if root == 0:
            node_curr = self.root
        if node_curr==Node: #goc = empty
            return []
        else:
            res =[]

            res_L = self.display_L_node_R(node_curr.left) #1
            for x in res_L:
                res.append(x)

            res.append(node_curr.key) #2

            res_R = self.display_L_node_R(node_curr.right) #3
            for x in res_R:
                res.append(x)
        return res

    # 4. Ham  DISPLAY: NLR
    def display_node_L_R(self, root=0):
        node_curr = root
        if root == 0:
            node_curr = self.root
        if node_curr == Node:  # goc = empty
            return []
        else:
            res = []
            res.append(node_curr.key) #1

            res_L = self.display_node_L_R(node_curr.left)#2
            for x in res_L:
                res.append(x)

            res_R = self.display_node_L_R(node_curr.right)#3
            for x in res_R:
                res.append(x)
        return res

    # 5. Ham  DISPLAY: LRN
    def display_L_R_node(self, root=0):
        node_curr = root
        if root == 0:
            node_curr = self.root
        if node_curr == Node:  # goc = empty
            return []
        else:
            res = []

            res_L = self.display_L_R_node(node_curr.left)#1
            for x in res_L:
                res.append(x)

            res_R = self.display_L_R_node(node_curr.right)#2
            for x in res_R:
                res.append(x)

            res.append(node_curr.key)  #3
        return res

    #6. Ham FIND
    def find(self,key):
        if self.root == None:
            return
        node_curr = self.root
        res_line = ''
        while(node_curr != None) and node_curr.key != key:
            res_line = res_line + f'{node_curr.key} -> '
            if key <= node_curr.key:
                node_curr = node_curr.left
            else:
                node_curr = node_curr.right
        if node_curr == None:
            return None
        else:
            res_line += res_line + f'{node_curr.key}'
            return res_line

#--------------------------------------
# n=int(input())
# arr=[int(input()) for x in range(1,n+1)]

n=5
arr = [3,2,1,5,4]
print(arr)

Tree = TreeNode()

for i in arr:
    Tree.inser(i)
res1 = Tree.display_L_node_R(Tree)
print('LNR',res1)

#TIM KIEM
while True:
    nhap = input('Nhap vao khoa can tim: ')
    if nhap == '':
        break
    val = int(nhap)
    res1 = Tree.find(val)
    if res1 == None:
        print(f'dont find {val}')
    else:
        print(f'find {val}: {res1}')

#-------------------------------------------------
