# Cho một dãy a gồm n số tự nhiên. Hãy đưa ra số tự nhiên nhỏ nhất chưa xuất hiện trong dãy.

# n = int(input())
# a = [int(input()) for i in range(n)]

arr = [0, 5, 1, 6, 2, 4, 3]
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
quickSort(arr,L,R)
print(arr)
def SearchMin(arr):
    check = 1
    if arr[0] > 0:
        return 0
    for i in range(1, n+1):
        if check not in arr:
            return check
        check += 1
print(SearchMin(arr))