from typing import List
#1. class Node
class ListNode:
    # Hàm khởi tạo đối tượng node
	#val=0 & next=None: tham so defaut
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#2. class Linked List
class LinkedList:
    #1. Hàm khởi tạo đối tượng Linked List
    def __init__(self, head=None):
        self.head = head

    # 2. Hàm append nút mới vào đầu DSLK đơn
    def append_element(self, new_data):
        # 1. Tạo node mới && truyen new_data cho nút mới
        new_node = ListNode(new_data)

        if not self.head:  # <=> <if self.head is None:>
            new_node.next = self.head
            self.head = new_node

        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
        # print(f'appended {new_node.data} to the list')

    # 3.0 Hàm In dữ liệu các nút, từ nút đầu của DSLK
    def display(self):
        temp = self.head
        while temp:
            print(temp.val, end=" ")
            temp = temp.next

    #4. Hàm insert new_node vào đúng index_k
    #4.1. Thêm phần tử vào đầu SINGLE LINKED LIST
    def insert_head(self,new_data):
        new_node = ListNode(new_data)
        new_node.next = self.head
        self.head = new_node

        return new_node.val

    #4.2. Thêm phần tử vào cuối SINGLE LINKED LIST
    def insert_tail(self,new_data):
        new_node = ListNode(new_data)
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        return temp.val

    #4.3. Thêm phần tử vào index_k
    def insert_mid(self, new_data, index_k):
        new_node = ListNode(new_data)
        next_node = None
        temp = self.head
        if index_k == 1:
            next_node = temp.next
            new_node.next = next_node
            temp.next = new_node
        else:
            for i in range(0, index_k-1):
                temp = temp.next
                next_node = temp.next
            new_node.next = next_node
            temp.next = new_node
        return temp.val

if __name__ == '__main__':
    # n = int(input())
    # data = [int(input()) for i in range(n)]
    # index_k = int(input())
    # new_data = int(input())
    n = 3
    data = [1,4,0]
    index_k = 2
    new_data = 5

    # 1. Tao ra node
    L = LinkedList()
    # 2. dua cac p.tu vao linked list
    for i in data:
        L.append_element(i)

    # 4. them p.tu vao dung index
    if index_k == 0:
        L.insert_head(new_data)
    elif index_k == n:
        L.insert_tail(new_data)
    elif 0 <= index_k <= n-1:
        L.insert_mid(new_data,index_k)
    else:
        print("Please enter 0 <= index_k <= n!!!")

    # 3. In cac p.tu trong linked list ra screen
    L.display()

