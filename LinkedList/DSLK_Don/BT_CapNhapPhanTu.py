'''
Nhập vào một số nguyên dương n, tiếp theo là n số nguyên của một dãy số, hãy cài đặt nó vào một danh sách liên kết đơn.
Tiếp theo nhập hai số nguyên a và b.
Hãy thay đổi giá trị của những phần tử có giá trị a thành giá trị b.
In ra màn hình danh sách đó, sau một phần tử có đúng một khoảng trắng.

Đầu vào  [1,1,2,2,3,3]   2    10
Đầu ra mong muốn    "1 1 10 10 3 3 "
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
        # print("None")

    #4. Hàm In dữ liệu các nút đúng index
    def display_index(self,index_k):
        count = 0
        temp = self.head
        while temp:
            if count == index_k:
                return f'display_index {index_k}: {temp.data}'
            temp = temp.next
            count += 1

    # 5. Hàm XÓA dữ liệu các nút đúng index
    def remove_index(self, index_k):
        count = 0
        temp = self.head
        while temp:
            if count == index_k:
                temp = temp.next
            if temp != None:
                count += 1
                print(temp.data, end=" ")
                temp = temp.next

    # 6. Hàm CAP NHAT PHAN TU
    def update_val(self, a, b):
        temp = self.head
        while temp:
            if temp.data == a:
                temp.data = b
                temp = temp.next
            else:
                temp = temp.next
        # print(f'appended {new_node.data} to the list')


# n = int(input())
# data = [int(input()) for i in range(n)]
#a = int(input())
#b = int(input())

n=6
data = [1,1,2,2,3,3]
a = 2
b =10

L = LinkedList()
for i in data:
    L.append_element(i)

#print theo yc đề bài:
L.update_val(a,b)
L.display()
