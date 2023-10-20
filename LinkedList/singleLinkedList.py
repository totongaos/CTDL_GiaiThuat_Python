class Node:
    def __init__(self,data=None):
        self.data = data # 1&2 phân bổ nút và đưa dữ liệu vào
        # 3 đặt tiếp theo là không có
        self.next = None

class Linked_List:
    def __init__(self):
        self.headNode = None

    def add_element_at_end(self,newdata):
        # 1&2 phân bổ nút và đưa dữ liệu vào
        # 3 đặt tiếp theo là không có
        NewNode = Node(newdata)
        if self.headNode is None:  # 4 nếu danh sách được liên kết là trống
            self.headNode = NewNode # hãy tạo nút mới làm đầu
            return
        # 5 đi qua cho đến node cuối
        last_element = self.headNode
        while last_element.next is not None:
            last_element = last_element.next
        # 6 thay đổi node tiếp theo của node cuối cùng
        last_element.next = NewNode

    def print_list(self):
        printval = self.headNode
        while (printval):
            print (printval.data,end=" ")
            printval = printval.next

n = 3
L1 = Linked_List()
for i in range(n):
    L1.add_element_at_end(str(input()))

L1.print_list()


