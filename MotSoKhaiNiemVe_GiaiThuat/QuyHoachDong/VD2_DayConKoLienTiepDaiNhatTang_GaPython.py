'''
Tìm ĐỘ DÀI (LEN) dãy con tăng dài nhất (Dãy đơn điệu tăng), **dãy con ko liên tiếp**
vd: [1,4,3,5,2] => dãy con là [1,3,5] -> len = 3
'''

#---------------------------------------------
#way 1:
#Ham dynamic_programming
def dynamic_programming(arr, n):
    # 1. tạo mảng lst luu tru cac đo dai cua day con
    lst = [0] * n
    lst[0] = 1

    # 2. xài 2 vòng lặp for lấy index < n && index < i
    for i in range(1, n):
        max_len = 0  # reset lại value max_len
        for j in range(0, i):
            if arr[j] < arr[i] and lst[j] > max_len:  # so sánh để tìm ra value max_len mới
                print('arr[j]<arr[i]', arr[j], arr[i], '\tlst[j] > max_len', lst[j], max_len)
                max_len = lst[j]
            lst[i] = max_len + 1  # lưu value max_len+1 tại index i vào mảng lst
    print(lst)

    # 3. return max(lst)
    return max(lst)

#1. input n & mang arr
# n = int(input())
# arr = [int(input()) for i in range(n)]
n = 5
arr = [1, 5, 3, 8, 0]

#2. chay ham dynamic_programming
print('max_len:',dynamic_programming(arr,n))