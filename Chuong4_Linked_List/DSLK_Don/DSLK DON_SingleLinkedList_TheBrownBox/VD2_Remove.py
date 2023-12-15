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

    #5. Hàm remove phần tử ở index_k
    #5.1. Xoa p.tu o đầu SINGLE LINKED LIST
    def remove_head(self):
        self.head = self.head.next

    #5.3. Xoa p.tu o index_k tu giua -> cuoi
    def remove_mid(self, index_k):
        curr = self.head
        if index_k == 1:
            curr.next = curr.next.next
        else:
            for i in range(1, index_k):
                curr = curr.next
            prev_node = curr
            next_node = curr.next
            prev_node.next = next_node.next
        return curr.val

if __name__ == '__main__':
    # n = int(input())
    # data = [int(input()) for i in range(n)]
    # index_k = int(input())
    n = 4
    data = [1,4,5,4]
    index_k = 1

    # 1. Tao ra node
    L = LinkedList()
    # 2. dua cac p.tu vao linked list
    for i in data:
        L.append_element(i)

    # 4. remove p.tu vao dung index
    if index_k == 0:
        L.remove_head()
        L.display()
    elif 0 <= index_k <= n-1:
        L.remove_mid(index_k)
        L.display()
    else:
        print("Please enter 0 <= index_k <= n-1 !!!")



