'''
Tìm ĐỘ DÀI (LEN) dãy con tăng dài nhất (Dãy đơn điệu tăng), **dãy con ko liên tiếp**
vd: [1,4,3,5,2] => dãy con là [1,3,5] -> len = 3
'''

#---------------------------------------------
#way 1:
#Ham dynamic_programming
def dynamic_programming(arr,n):
    #1. tạo 1 list lst với len = n
    lst = [0]*n
    lst[0] =1
    #2. xài vòng lặp for lấy index <n
    for i in range(1,n):
        max_len = 0 #2.1 tạo biến max_len đo độ dài của mảng con
        #2.2 xài vong lặp for lấy index < i:
        for j in range(0,i):
            #2.2.1 check arr[i] với các index nhỏ hơn i -> có nhỏ hơn arr[i] ko?
            if arr[j]<arr[i]:
                # print('arr[j]<arr[i]',arr[j],arr[i])
                #check phần tử lst[j] với biến max_len
                if lst[j]>max_len:
                    print(lst[j], max_len)
                    max_len=lst[j] #nếu max_len < thì max_len = lst[j]
            #2.2.2 lưu lst[i] = max_len + 1
            lst[i] = max_len+1
    print(lst)
    #3. return max(lst)
    return max(lst)

#1. input n & mang arr
# n = int(input())
# arr = [int(input()) for i in range(n)]
n = 5
arr = [7, 5, 3, 8, 0]

#2. chay ham dynamic_programming
print('max_len:',dynamic_programming(arr,n))