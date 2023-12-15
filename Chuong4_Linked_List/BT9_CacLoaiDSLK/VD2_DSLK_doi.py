#1. Khởi tạo class DS: gán value = val; gán 2 con trỏ next & prev thành None
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

    #2. Hàm add_node(): chèn node_to_add vào DSLK sau next_node
    def insert_node(next_node, node_to_add):
        # 2.1 Gọi node_to_add có tên là pre_node, trỏ con trỏ prev của next_node tới prev_node
        prev_node = next_node.prev
        # 2.2 Gán con trỏ next && prev của node_to_add vào vị trí phù hợp
        node_to_add.next = next_node
        node_to_add.prev = prev_node
        # 2.3 Gán con trỏ next của pre_node vào vị trí phù hợp
        prev_node.next = node_to_add
        # 2.4 Gán con trỏ prev của next_node vào vị trí phù hợp
        next_node.prev = node_to_add
        print(f'inserted {node_to_add.val} to the list')
        return next_node.val,node_to_add.val
    #3. Hàm delete_node(): xóa node trong ListNode
    def delete_node(node):
        # 3.1 Lưu con trỏ prev của node vào prev_node
        prev_node = node.prev
        # 3.2 Lưu con trỏ next của node vào next_node
        next_node = node.next
        # 3.3 Thiết lập con trỏ next của prev_node trỏ tới next_node
        prev_node.next = next_node
        # 3.4 Thiết lập con trỏ prev của next_node trỏ tới prev_node
        next_node.prev = prev_node
        print(f'removed {node.val} from the list')
#-------------------------------------------
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

#-------------------------------------------
#insert phần tử vào trước vị trí x
insert_node = ListNode.insert_node(tail,five)
#print các phần tử trong link list ra
print(insert_node)
print(head.val,end=" ")
print(head.next.val,end=" ")
print(head.next.next.val)
insert_node = ListNode.insert_node(five,two)
print(insert_node)
print(head.val,end=" ")
print(head.next.val,end=" ")
print(head.next.next.val, end=" ")
print(head.next.next.next.val)
#-------------------------------------------
#xóa phần tử
delete_node = ListNode.delete_node(two)
#print các phần tử trong link list ra
print(head.val,end=" ")
print(head.next.val,end=" ")
print(head.next.next.val)
