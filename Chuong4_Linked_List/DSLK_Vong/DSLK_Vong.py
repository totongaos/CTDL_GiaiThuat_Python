'''
Nhập vào một số nguyên dương n, tiếp theo là n số nguyên của một dãy số, hãy cài đặt nó vào một danh sách liên kết vòng.
Tiếp theo cho một số nguyên k, (0 ≤ k < n).
Hãy in ra màn hình các phần tử ở chỉ số k đến n-1 rồi từ chỉ số 0 đến k-1, sau một phần tử có một khoảng trắng.
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

    #4. Hàm In dữ liệu các nút đúng index
    def display_index(self,index_k):
        count = 0
        temp = self.head
        res = ''
        for i in range(index_k): #tim val dung truoc index_k
            temp = temp.next
        while temp:
            res += str(temp.data) + " "
            temp = temp.next
        temp2 = self.head
        for i in range(0,index_k): #tim val dung truoc index_k
            res += str(temp2.data) + " "
            temp2 = temp2.next
        return res

# n = int(input())
# data = [int(input()) for i in range(n)]
#index_k = int(input())

n=6
data = [1,2,3,4,5,6]
index_k = 2

L = LinkedList()
for i in data:
    L.append_element(i)

#print theo yc đề bài:
print(L.display_index(index_k))
