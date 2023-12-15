# Nhập và một số nguyên dương n, tiếp theo là n số nguyên lần lượt là các phần tử của một dãy số,
# hãy đếm tần số (số lần xuất hiện) của các số trong dãy và in nó ra màn hình dưới dạng sau: "a1 t1; a2 t2; ... an tn; ",
# trong đó t1 là số lần xuất hiện của số a1, t2 là số lần xuất hiện của a2, ... a1, a2, .. an không trùng nhau
# và được sắp xếp tăng dần (xem ví dụ để rõ hơn).

# n = int(input())
# a = [int(input()) for i in range(n)]

arr = [-3, -3, 2, 4, 2, 2, 6]
n=7

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
        while (arr[i] < pivot):
            i+=1
        #Biến j sẽ chạy từ R -> L; xài while với dk arr[j] <= pivot thì dừng
        while (arr[j] > pivot):
            j-=1
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

#way 1:
quickSort(arr,L,R)
def frequency(arr):
    count = 1
    for i in range(1, n):
        if arr[i] == arr[i-1]:
            count += 1
        else:
            print(f'{arr[i-1]} {count}', end="; ")
            count = 1
    print(f'{arr[n - 1]} {count}', end="; ")
frequency(arr)


#way 2:
# quickSort(arr,L,R)
# def frequency(arr):
#     for i in range(1, n):
#         if arr[i] != arr[i-1]:
#             print(f'{arr[i-1]} {arr.count(arr[i-1])}', end="; ")
#     print(f'{arr[n-1]} {arr.count(arr[n-1])}', end="; ")
# frequency(arr)