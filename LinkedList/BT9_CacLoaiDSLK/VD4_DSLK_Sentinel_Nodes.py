class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

    # 2. Hàm add_to_end(): dùng để thêm nút node_to_add vào cuối DSLK đôi
    def add_to_end(node_to_add):
        node_to_add.next = tail  # 2.1 Thiết lập con trỏ next của node_to_add thành tail
        node_to_add.prev = tail.prev  # 2.2 Thiết lập con trỏ prev của node_to_add là tail.prev
        tail.prev.next = node_to_add  # 2.3  Cập nhật con trỏ next của nút trước tail để trỏ đến node_to_add
        tail.prev = node_to_add  # 2.4  Cập nhật con trỏ prev của tail để trỏ đến node_to_add
        print(f'inserted {node_to_add.val} to the list to end')
        return node_to_add.val

    # 3. Hàm remove_from_end() dùng để xóa nút cuối cùng
    def remove_from_end():
        if head.next == tail:  # 3.1 Kiểm tra xem danh sách có ít nhất 2 nút hay không
            print('the list empty')
            return

        node_to_remove = tail.prev  # 3.2. Thiết lập nút node_to_remove thành tail.prev
        node_to_remove.prev.next = tail  # 3.3. Thiết lập nút node_to_remove.prev.next thành tail
        tail.prev = node_to_remove.prev  # 3.4. Thiết lập nút tail.prev thành node_to_remove.prev
        print(f'removed {node_to_remove.val} the list from end')
        return node_to_remove.val

    def add_to_start(node_to_add):
        node_to_add.prev = head
        node_to_add.next = head.next
        head.next.prev = node_to_add
        head.next = node_to_add
        print(f'inserted {node_to_add.val} to the list to start')
        return node_to_add.val


    def remove_from_start():
        if head.next == tail:
            print('the list empty')
            return

        node_to_remove = head.next
        node_to_remove.next.prev = head
        head.next = node_to_remove.next
        print(f'removed {node_to_remove.val} the list from end')
        return node_to_remove.val

#tạo các biến để add phần tử vào link list
head = ListNode(None)
tail = ListNode(None)
one = ListNode(1)
two = ListNode(2)
three = ListNode(3)
five = ListNode(5)
#tạo các nút next, prev cho 2 phần tử head, tail
head.next = tail
tail.prev = head

#add phần tử vào Linked List
add_to_end = ListNode.add_to_end(one)
add_to_start = ListNode.add_to_start(two)
#remove phần tử khỏi Linked List
remove_from_start = ListNode.remove_from_start()
#print các phần tử trong link list ra
print(head.val,end=" ")
print(head.next.val,end=" ")
print(head.next.next.val,end=" ")
