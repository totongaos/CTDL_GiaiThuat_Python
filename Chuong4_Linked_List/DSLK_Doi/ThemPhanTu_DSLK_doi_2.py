'''
Nhập vào một số nguyên dương n, tiếp theo là n số nguyên của một dãy số,
hãy cài đặt nó vào một danh sách liên kết đôi. Tiếp theo cho hai số nguyên k và x, (0 ≤ k ≤ n).
Hãy chèn giá trị x vào danh sách liên kết tại chỉ số k và in ra màn hình danh sách đó,
sau một phần tử có đúng một khoảng trắng.

Input:  [1,2,3]    0    10    |||    Actual output:   "10 1 2 3 "
'''

#1. class Node
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

#2. Khởi tạo class DS: gán value = val; gán 2 con trỏ next & prev thành None
class ListNode:
    def __init__(self):
        self.head = None
        self.tail = None
    #1. Tạo một node trong dánh sách liên kết đôi l với giá trị của node đầu là x
    def createList(x):
        l = ListNode
        l.head = Node(x)
        l.head.val = x
        l.head.prev = None
        l.head.next = None
        l.tail = l.head
        return l.head.val
    #2. Thêm phần tử vào đầu douList.
    def addHead(x):
        l = ListNode
        temp = Node(x)
        temp.val = x
        temp.prev = None
        temp.next = l.head
        l.head.prev = temp
        l.head = temp
        return temp.val

    #3. Thêm phần tử vào cuối dánh sách liên kết đôi.
    def addTail(x):
        l = ListNode
        temp = Node(x)
        temp.val = x
        temp.next = None
        temp.prev = l.tail
        l.tail.next = temp
        l.tail = temp
        return temp.val

    # 5. Thêm phần tử vào giữa dánh sách liên kết đôi.
    def insertIndex(x, index_k):
        l = ListNode
        p = l.head
        for i in range(1,index_k):
            p = p.next
        temp = Node(x)
        temp.val = x
        temp.prev = p
        temp.next = p.next
        p.next.prev = temp
        p.next = temp
        return temp.val

    #4. Display theo phần tử đầu
    def display_head():
        l = ListNode
        temp = l.head
        while temp:
            print(temp.val, end=" ")
            temp = temp.next

#-------------------------------------------
# n=int(input())
# arr=[int(input()) for x in range(1,n+1)]
# index_k=int(input())
# x=int(input())


n=3
arr = [1,2,3]
index_k = 0
x = 10
L = ListNode.createList(arr[0])
for i in arr[1:]:
    L = ListNode.addTail(i)

if index_k == 0:
    L = ListNode.addHead(x)
elif index_k == n :
    L = ListNode.addTail(x)
else:
    L = ListNode.insertIndex(x, index_k)

ListNode.display_head()
