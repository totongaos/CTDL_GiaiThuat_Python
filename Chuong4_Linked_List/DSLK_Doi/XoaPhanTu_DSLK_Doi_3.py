'''
Nhập vào một số nguyên dương n, tiếp theo là n số nguyên của một dãy số, hãy cài đặt nó vào một danh sách liên kết đơn.
Tiếp theo cho một số nguyên k, (0 ≤ k < n).
Hãy xóa phần tử ở chỉ số k và in ra màn hình danh sách đó, sau một phần tử có đúng một khoảng trắng.

Đầu vào [1,2,3,4]  1
Đầu ra thực tế "1 3 4 "
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
    def createList(self,x):
        self.head = Node(x)
        self.head.val = x
        self.head.prev = None
        self.head.next = None
        self.tail = self.head
        return self.head.val
    #2. Thêm phần tử vào đầu douList.
    def addHead(self,x):
        temp = Node(x)
        temp.val = x
        temp.prev = None
        temp.next = self.head
        self.head.prev = temp
        self.head = temp
        return temp.val

    #3. Thêm phần tử vào cuối dánh sách liên kết đôi.
    def addTail(self,x):
        temp = Node(x)
        temp.val = x
        temp.next = None
        temp.prev = self.tail
        self.tail.next = temp
        self.tail = temp
        return temp.val

    # 5. Thêm phần tử vào index_k
    def insertIndex(self,x, index_k):
        # l = ListNode
        p = self.head
        for i in range(1,index_k):
            p = p.next
        temp = Node(x)
        temp.val = x
        temp.prev = p
        temp.next = p.next
        p.next.prev = temp
        p.next = temp
        return temp.val

    # 6. XÓA phần tử vào index_k
    def remove_head(self, k): #6.1 xóa phần tử đầu
        val_next = self.head.next
        val_next.prev = None
        self.head = val_next

    def remove_tail(self, k): #6.2 xóa phần tử cuối
        val_prev = self.tail.prev
        val_prev.next = None
        self.tail = val_prev

    def xoa(self, index_k): #6.3 xóa những phần tử ở giữa
        val_prev = self.head
        for i in range(1,index_k): #tim val dung truoc index_k
            val_prev = val_prev.next

        temp = val_prev.next
        val_next = temp.next
        val_prev.next = val_next
        val_next.prev = val_prev

    #4. Display theo phần tử đầu
    def display_head(self):
        temp = self.head
        while temp:
            print(temp.val, end=" ")
            temp = temp.next

#-------------------------------------------
# n=int(input())
# arr=[int(input()) for x in range(1,n+1)]
# index_k=int(input())

n=5
arr = [1,4,5,6,3]
index_k = 2

L = ListNode
L.createList(L,arr[0])
for i in arr[1:]:
    L.addTail(L,i)
if index_k == 0:
    L.remove_head(L,index_k)
elif index_k == n -1:
    L.remove_tail(L,index_k)
else:
    L.xoa(L,index_k)

L.display_head(L)
