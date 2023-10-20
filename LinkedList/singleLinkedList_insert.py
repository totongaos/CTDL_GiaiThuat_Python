class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self): #tạo 1 node rỗng
        self.head = None
        self.tail = None

    def add_Value(self, value):
        nodeNew = Node(value) #khai báo node mới là class Node
        if self.head == None: #them value vào list khi mà list empty
            self.head = nodeNew # Cho head trỏ tới nodeNew
            self.tail = nodeNew # Cho tail trỏ tới nodeNew
        else: #them value vào cuối list khi mà list có value
            self.tail.next = nodeNew  #Cho next trỏ tới nodeNew
            self.tail = nodeNew  # Cho head trỏ tới nodeNew
    def insert_Value(self, index, value):
        node_New = Node(value)
        previous_Pointer = None
        current_element = self.head
        i = 0
        while i < index and current_element != None:
            i+=1
            previous_Pointer = current_element
            current_element = current_element.next
        if previous_Pointer == None: #them vào dau danh sach
            node_New.next = self.head # cập nhật lại node_new tiếp = con trỏ đầu
            self.head = node_New #con trỏ đầu trỏ đến nút new
            if self.tail == None: #cho case lstNode chỉ có 1 phần tử
                self.tail = node_New
        else:
            if current_element == None:
                #them vào cuoi DS
                self.tail.next = node_New  # cập nhật lại node_new tiếp = con trỏ đuôi
                self.tail = node_New #con trỏ đuôi trỏ đến nút new
            else:
                #them vào giưa DS
                previous_Pointer.next = node_New  # cập nhật lại node_new tiếp = con trỏ trước
                node_New.next = current_element # cập nhật lại con trỏ hiện tại tiếp = node new tiếp theo

    def print_List(self):
        printval = self.head #khai báo printval là node đầu
        while (printval):
            print (printval.value,end=" ") #print từng node printval
            printval = printval.next #khai báo printval là số tiếp theo trong self.head

if __name__ == '__main__':
    # khai báo lst là class LinkedList
    L1 = LinkedList()
    n = int(input())

    # a - add value
    for i in range(n):
        L1.add_Value(str(input()))

    # b - insert value
    index_k = int(input())
    numX = int(input())
    # print(f'chen {numX} vao vi tri {index_k}')
    L1.insert_Value(index_k, numX)
    L1.print_List()