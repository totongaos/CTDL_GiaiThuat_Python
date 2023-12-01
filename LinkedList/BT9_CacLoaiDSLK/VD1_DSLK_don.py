#1. Khởi tạo class DS: gán value = val; gán con trỏ next thành None
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

    #2. Hàm add_node(): chèn node_to_add vào DSLK giữa prev_node && nút kế tiếp của prev_node
    def insert_node(prev_node, node_to_add):
        #2.1 Gán con trỏ next của node_to_add = con trỏ next của prev_node
        node_to_add.next = prev_node.next
        #2.2 Gán con trỏ next của prev_node = node_to_add
        prev_node.next = node_to_add
        print(f'inserted {node_to_add.val} to the list')
        return prev_node.val, node_to_add.val
    #3. Hàm delete_node(): xóa prev_node trong ListNode sau vị trí x
    def delete_node(prev_node):
        #3.1 Gán con trỏ next của con trỏ của prev_node = con trỏ next của prev_node.next
        prev_node.next = prev_node.next.next
        print(f'removed {prev_node.val} from the list')
#-------------------------------------------
#tạo các biến để add phần tử vào link list
head = ListNode(None)
one = ListNode(1)
two = ListNode(2)
three = ListNode(3)
five = ListNode(5)

#-------------------------------------------
#insert phần tử vào trước vị trí x
insert_node = ListNode.insert_node(head,two)
insert_node = ListNode.insert_node(head,five)
insert_node = ListNode.insert_node(five,three)
#print các phần tử trong link list ra
print(head.val,end=" ")
print(head.next.val,end=" ")
print(head.next.next.val,end=" ")
print(head.next.next.next.val)
#-------------------------------------------
#xóa phần tử sau vị trí x
delete_node = ListNode.delete_node(three)
#print các phần tử trong link list ra
print(head.val,end=" ")
print(head.next.val,end=" ")
print(head.next.next.val,end=" ")

