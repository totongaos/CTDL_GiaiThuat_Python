# Nhập vào số nguyên dương n, tiếp theo là n số nguyên của dãy số a.
# Hãy sắp xếp dãy số a thành dãy không giảm (số sau không bé hơn số trước) và in dãy đó ra màn hình,
# sau mỗi phần tử có đúng một khoảng trắng.

# n = int(input())
# a = [int(input()) for i in range(n)]

arr = [1, 5, 5, 6, 7, 4 , 5, 2]
n=8
#Khởi tạo biến L & R
L = 0
R = len(arr) - 1
def quickSort(arr,L,R):
    i,j = L,R
    #Xác định phần tử chốt trong dãy
    pivot = arr[(L + R) // 2]
    # vì i sẽ chạy từ L & j ngc lại -> i<j
    while i<j:
        #Biến i sẽ chạy từ L -> R; xài while với dk arr[i] >= pivot thì dừng
        while (arr[i] < pivot): i+=1
        #Biến j sẽ chạy từ R -> L; xài while với dk arr[j] <= pivot thì dừng
        while (arr[j] > pivot): j-=1
        #vì i sẽ chạy từ L & j ngc lại -> i<=j
        if (i <= j):
            #hoán đổi vị trí của 2 phần tử
            arr[i], arr[j] = arr[j], arr[i]
            i+=1
            j-=1

    #xai đê quỵ chỉnh lại L & R
    if i < R:
        quickSort(arr,i,R)
    if L < j:
        quickSort(arr,L,j)
    return arr

print(quickSort(arr,L,R))