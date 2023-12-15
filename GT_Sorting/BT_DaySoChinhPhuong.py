# Nhập và một số nguyên dương n, tiếp theo là n số nguyên của dãy số a.
# Hãy in ra các số chính phương*  có trong dãy theo thứ tự tăng dần (phía sau mỗi phần tử có đúng một khoảng trắng),
# nếu không tồn tại số chính phương nào trong dãy a thì in ra "NULL".
#
# *Số chính phương là số có thể biểu diễn được dưới dạng bình phương của một số nguyên ví dụ 0, 1, 4, 9, 16, ... là các số chính phương.

#way 1: ko xài giai thuat
# def check(x):
#     y=x**0.5
#     if int(y)==y: return True
#     return False
# def star(x):
#     count=0
#     for i in x:
#         if check(i)==True: count+=1;print(i,end=" ")
#     if count==0: print("NULL")
# s=[int(input()) for i in range(int(input()))]
# s=sorted(s);m=[]
# for i in s:
#     if i not in m: m.append(i)
# star(m)

#way 3: xài giai thuat quick
def quickSort(arr,L,R):
    i,j = L,R
    pivot = arr[(L+R)//2]
    while i<j:
        while arr[i] < pivot:
            i+=1
        while pivot < arr[j]:
            j-=1
        if i<=j:
            arr[i],arr[j] = arr[j],arr[i]
            i+=1
            j-=1
    if i<R:
        quickSort(arr,i,R)
    if L<j:
        quickSort(arr,L,j)
    return arr

def squareNum(num):
    k = int(num ** 0.5)
    if k*k == num: return True
    return False
def printArray(new_arr):
    count = 0
    for i in new_arr:
        if squareNum(i): count+=1;print(i,end=" ")
    if count == 0: print("NULL")

n= 5
arr = [9,1,2,3,1]
new_arr = []
L=0
R=n-1
quickSort(arr,L,R)
# print(arr)
for i in arr:
    if i not in new_arr:
        new_arr.append(i)
printArray(new_arr)





#way 2: xài giai thuat quick
# def quickSort(arr,L,R):
#     i,j = L,R
#     pivot = arr[(L+R)//2]
#     while i<j:
#         while arr[i] < pivot:
#             i+=1
#         while pivot < arr[j]:
#             j-=1
#         if i<=j:
#             arr[i],arr[j] = arr[j],arr[i]
#             i+=1
#             j-=1
#     if i<R:
#         quickSort(arr,i,R)
#     if L<j:
#         quickSort(arr,L,j)
#     return arr
#
#
# def squareNum(arr, new_arr):
#     for i in range(0, len(arr)):
#         k = int(arr[i] ** 0.5)
#         if k*k == arr[i]:
#             if arr[i] not in new_arr:
#                 new_arr.append(arr[i])
#     return new_arr
#
#
# # n = int(input())
# # arr = [int(input()) for i in range(n)]
#
# n= 5
# arr = [9,1,2,3,1]
# new_arr = []
#
# L=0
# R=n-1
#
# quickSort(arr,L,R)
# print(arr)
#
# squareNum(arr, new_arr)
# print(new_arr)
#
# if len(new_arr)>0:
#     print(*new_arr)
# else:
#     print('NULL')
