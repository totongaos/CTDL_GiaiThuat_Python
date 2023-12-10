'''
Nhập vào một số nguyên dương n, hãy cài đặt một danh sách lên kết đôi để lưu các số từ n giảm về 1 và từ 1 răng đến n (xem ví dụ để rõ hơn).
In ra danh sách liên kết đó, phía sau mỗi phần tử có một khoảng trắng.

Input:  3    |||    Actual output:   "3 2 1 2 3 "
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

    #4. Display theo phần tử đầu
    def display_head():
        l = ListNode
        temp = l.head
        while temp:
            print(temp.val, end=" ")
            temp = temp.next

#-------------------------------------------
# n=int(input())
n=3
L = ListNode.createList(1)
for i in range(2,n+1):
    L = ListNode.addHead(i)
    L = ListNode.addTail(i)

ListNode.display_head()
