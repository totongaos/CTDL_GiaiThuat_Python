# Ví dụ 5: hãy tính tổng tất cả các giá trị trong danh sách liên kết số nguyên:

#class LinkedList
class ListNode:
    #Hàm add từng phần tử val vào link list
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
    #Hàm tính sum các phần tử val trong link list = sử dụng vòng lặp while
    def get_sum(head):
        ans = 0
        dummy = head
        while dummy:
            ans += dummy.val
            dummy = dummy.next
        return ans

#tạo các biến để add phần tử vào link list
head = ListNode(None)
one = ListNode(1)
two = ListNode(2)
three = ListNode(3)
#tạo các nút next cho các phần tử mới add
one.next = two
two.next = three

#tạo biến sum_s tính sum các phần tử từ biến truyền vào đến cuối link list
sum_s1 = ListNode.get_sum(two)
#print kqua ra màn hình
print(sum_s1)
