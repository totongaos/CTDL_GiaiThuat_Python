'''
Một người nông dân muốn trồng hoa trong vườn của mình.
Để khu vườn thêm màu sắc, ông quyết định trồng nhiều loại hoa khác nhau trong vườn.
Mỗi loài hoa có một cách trồng khác nhau nên ông sẽ trồng từng bông hoa vào những ngày liền nhau.
Cháu trai của ông đã rất mong được nhìn thấy tất cả những bông hoa trong vườn nở rộ tuyệt vời như thế nào.
Tuy nhiên, mỗi loài hoa có thời gian phát triển khác nhau từ khi trồng đến khi nở.
Cho dãy a gồm n số nguyên dương lần lượt là thời gian phát triển của các bông hoa.
Nhiệm vụ của bạn là giúp người nông dân tìm ra ngày hoa nở sớm nhất.
'''


#Hàm giải thuật tham lam - way 1 - sử dụng hàm max()
def algorithm1(n,arr):
    count_days = 1
    sum_days = 0
    for i in reversed(range(0, n)):
        sum_days = max(sum_days, arr[i] + count_days)
        count_days += 1
    return sum_days

#Hàm giải thuật tham lam - way 2 - sử dụng lệnh if
def algorithm2(n,arr):
    count_days = 1
    sum_days = 0
    for i in reversed(range(0, n)):
        if arr[i] + count_days > sum_days:
            sum_days = arr[i] + count_days
        count_days += 1
    return sum_days

#1. input n & mảng arr
# n = int(input())
# arr = [int(x) for x in input().split()]
#1. input n & mang arr
# n = int(input())
# arr = [int(input()) for i in range(n)]
n =4
arr = [4, 1, 3, 1]

#2. sắp xếp mảng
arr.sort()
#3. print kqua sử dung function algorithm đã viết ở trên
print(algorithm1(n,arr))
# print(algorithm2(n,arr))

#-----------------------------------------------------------------
#WAY 3: so sánh max(arr) với n
#1. input n & mảng arr
# n = int(input())
# arr = [int(x) for x in input().split()]
#1. input n & mang arr
# n = int(input())
# arr = [int(input()) for i in range(n)]
n =4
arr = [4, 1, 3, 1]
def sum_days(n,arr):
    if max(arr)>n:
        return max(arr)+1
    else:
        return n + 1
print(sum_days(n,arr))