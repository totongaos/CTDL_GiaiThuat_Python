from typing import List
class ListNode(object):
    def __init__(self, val=0, next=None): #val=0 & next=None: tham so defaut
        self.val = val
        self.next = next

if __name__ == '__main__':
    #1. Tao ra 3 node
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)

    #2. noi cac node lai voi nhau
    n1.next = n2
    n2.next = n3

    print("Linked List:", end=" ")
    #3. duyet cac p.tu trong linked list
    pHead = n1
    while pHead:
        print(pHead.val, end=" ")
        pHead = pHead.next