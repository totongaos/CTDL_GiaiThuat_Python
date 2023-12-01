'''
Anh Lộc làm nghề phụ hồ cho một công ty xây dựng, Anh nhận thấy rằng mỗi loại gạch đều có độ cứng khác nhau.
Giả sử rằng viên gạch có độ cứng k chỉ có thể chịu được tối đa k viên gạch khác chồng lên nó, nếu nhiều hơn thì nó sẽ bị vỡ.

Cho mảng a gồm n số nguyên dương lần lượt là độ cứng của các viên gạch.

Anh Lộc muốn lấy gạch và xếp chúng chồng lên nhau thành một chồng gạch cao nhất có thể mà không để vỡ viên gạch nào

Hãy tìm và in ra màn hình xem anh Lộc có thể xếp chồng gạch có độ cao lớn nhất là bao nhiêu.
'''

#-----------------------------------------------------------------
#Hàm giải thuật tham lam - way 1
def algorithm(n,arr):
    stiffness = max(arr)
    count = 1
    if stiffness < n:
        for i in reversed(range(0, n)):
            stiffness -= 1
            count += 1
            if stiffness == 0: return count
    return n

#1. input n & mảng arr
# n = int(input())
# arr = [int(x) for x in input().split()]
#1. input n & mang arr
# n = int(input())
# arr = [int(input()) for i in range(n)]
n =5
arr = [1,1,1,1,1]
#2. sắp xếp mảng
arr.sort()
#3. print kqua sử dung function algorithm đã viết ở trên
print(algorithm(n,arr))