'''
reverse a singly linked list
'''

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

    #6. Hàm  reverse (while) a singly linked list
    def reverse(self): #WAY 1:
        prev = None
        curr_node = self.head

        while curr_node:
            next_node = curr_node.next
            curr_node.next = prev
            prev = curr_node
            curr_node = next_node
        self.head = prev

    def reverse(self): #WAY 2:
        temp = self.head
        curr_node = temp

        while curr_node!=None and curr_node.next!=None:
            next_node = curr_node.next
            curr_node.next = next_node.next
            next_node.next = temp
            temp = next_node
        self.head = temp

if __name__ == '__main__':
    # n = int(input())
    # data = [int(input()) for i in range(n)]
    n = 3
    data = [1,4,0,8]

    # 1. Tao ra node
    L = LinkedList()
    # 2. dua cac p.tu vao linked list
    for i in data:
        L.append_element(i)

    #6. reverse a singly linked list
    L.reverse()

    #3. In mang ra
    print("In linked list", end=" ")
    L.display()

