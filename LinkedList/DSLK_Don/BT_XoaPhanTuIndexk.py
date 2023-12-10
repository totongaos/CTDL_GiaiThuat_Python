'''
Nhập vào một số nguyên dương n, tiếp theo là n số nguyên của một dãy số, hãy cài đặt nó vào một danh sách liên kết đơn.
Tiếp theo cho một số nguyên k, (0 ≤ k < n), hãy xóa phần tử ở chỉ số k và in ra màn hình danh sách đó,
sau một phần tử có một khoảng trắng.
Đầu vào  [1,2,3]  2
Đầu ra mong muốn   "1 2 "
'''

#1. class Node
class Node:
    # Hàm khởi tạo đối tượng nút
    def __init__(self, data):
        self.data = data
        self.next = None

#2. class Linked List
class LinkedList:
    #1. Hàm khởi tạo đối tượng Linked List
    def __init__(self):
        self.head = None

    #2. Hàm append_element chèn nút mới vào đầu DSLK đơn
    def append_element(self,new_data):
        #1. Tạo node mới && đặt dữ liệu cho nút mới
        new_node = Node(new_data)
        #2. dùng if check DSLK có rỗng ko?
        if not self.head:  # <=> code tương đương: 'if self.head is None:'
            self.head = new_node #2.1.1 nếu DSLK rỗng: cho đầu DS head = nút mới tạo
        else: #2.2 ngc lại
            temp = self.head #2.2.1 tạo biến temp = cho đầu DS head
            while temp.next: #2.2.2 khi biến temp.next có giá trị != None
                temp = temp.next # cho biến temp = giá trị next
                # print(temp.data)
            temp.next = new_node #2.2.3 giá trị temp.next = giá trị node mới
        # print(f'appended {new_node.data} to the list')

    #3. Hàm In dữ liệu các nút, từ nút đầu của DSLK
    def display(self):
        temp = self.head
        while temp:
            print (temp.data, end=" ")
            temp = temp.next

    #4. Hàm In dữ liệu các nút đúng index
    def display_index(self,index_k):
        count = 0
        temp = self.head
        while temp:
            temp = temp.next
            if count == index_k - 1:
                print(f'display_index {index_k}: {temp.data}', end=" ")
            count += 1

    # 5. Hàm display ẩn dữ liệu ở index
    def display_hidden_index(self, index_k):
        count = 0
        temp = self.head
        while temp:
            if count == index_k:
                temp = temp.next
            if temp!=None:
                count += 1
                print(temp.data, end=" ")
                temp = temp.next

    #6. Hàm Xóa phần tử đầu tiên của danh sách liên kết đơn.
    def xoa(self, k):
        hien_tai = self.head
        if k == 0:
            self.head = self.head.next
        else:
            for i in range(1, k):  # tim val dung truoc index_k
                hien_tai = hien_tai.next
            truoc = hien_tai
            hien_tai = hien_tai.next
            truoc.next = hien_tai.next

# n = int(input())
# data = [int(input()) for i in range(n)]
# index_k = int(input())
data = [1,2,3]
index_k = 2

L = LinkedList()
for i in data:
    L.append_element(i)

#print theo yc đề bài: đưa ra giá trị phần tử ở chỉ số k.
# L.remove_index(index_k)
L.xoa(index_k)
L.display()
