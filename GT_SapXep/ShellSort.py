# Nhập vào số nguyên dương n, tiếp theo là n số nguyên của dãy số a.
# Hãy sắp xếp dãy số a thành dãy không giảm (số sau không bé hơn số trước) và in dãy đó ra màn hình,
# sau mỗi phần tử có đúng một khoảng trắng.

# n = int(input())
# a = [int(input()) for i in range(n)]

arr = [9, 1, 3, 7, 8, 4, 2, 6, 5]
n=9

def sellSort(arr,n):
    interval = (n // 2)
    # k =0
    #lap lại den khi interval = 0
    while interval>0:
        #lap qua tat cả cac phan tu trong mảng arr
        for i in range(interval,n):
            # k += 1
            # print(f'i {k}',i)
            #lay gia tri phan tu dang xet
            temp = arr[i]
            #so sánh với tất cả các phần tử trước đó
            index_j = i
            while index_j >= interval and arr[index_j-interval]>temp:
                # doi vi tri cho 2 phan tu voi nhau
                arr[index_j], arr[index_j-interval] = arr[index_j-interval], arr[index_j]
                index_j -= interval

        interval //= 2
    return arr

print(sellSort(arr,n))