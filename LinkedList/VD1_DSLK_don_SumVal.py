# Ví dụ 1: hãy tính tổng tất cả các giá trị trong danh sách liên kết số nguyên:



#class LinkedList
class ListNode:
    #Hàm add từng phần tử val vào link list
    def __init__(self, val):
        self.val = val
        self.next = None
    #Hàm tính sum các phần tử val trong link list = sử dụng vòng lặp while
    def get_sum1(head):
        ans = 0
        while head:
            ans += head.val
            head = head.next
        return ans

    # Hàm tính sum các phần tử val trong link list = sử dụng thực hiện đệ quy
    def get_sum2(head):
        if not head:
            return 0
        return head.val + ListNode.get_sum2(head.next)

#tạo các biến để add phần tử vào link list
one = ListNode(1)
two = ListNode(2)
three = ListNode(3)
#tạo các nút next cho các phần tử mới add
one.next = two
two.next = three
head = one #biến đầu tiên luôn nào head

#print các phần tử trong link list ra
print(head.val)
print(head.next.val)
print(head.next.next.val)

#tạo biến sum_s tính sum các phần tử từ biến truyền vào đến cuối link list
sum_s1 = ListNode.get_sum1(two)
#print kqua ra màn hình
print(sum_s1)

#tạo biến sum_s tính sum các phần tử từ biến truyền vào đến cuối link list
sum_s2 = ListNode.get_sum2(head)
#print kqua ra màn hình
print(sum_s2)