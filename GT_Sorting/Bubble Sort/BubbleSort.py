# Nhập vào số nguyên dương n, tiếp theo là n số nguyên của dãy số a.
# Hãy sắp xếp dãy số a thành dãy không giảm (số sau không bé hơn số trước) và in dãy đó ra màn hình,
# sau mỗi phần tử có đúng một khoảng trắng.

# n = int(input())
# a = [int(input()) for i in range(n)]

arr = [3,2,1,5]
n =4

# def bubbleSort(arr):
#     for j in range(1, len(arr)):
#         for i in range(1,len(arr)):
#             if arr[i] < arr[i-1]:
#                 arr[i-1], arr[i] = arr[i], arr[i - 1]
#     return arr
#
# print(*bubbleSort(arr))


#   WAY 2
# cach nay se nhanh hon chut nho bien swapped
# n = int(input())
# arr = [int(input()) for i in range(n)]
#
def bubbleSort(arr):
    for j in range(1, len(arr)):
        swapped = True
        for i in range(1,len(arr)):
            if arr[i] < arr[i-1]:
                arr[i-1], arr[i] = arr[i], arr[i - 1]
                swapped = False
        if swapped:
            break
    return arr

print(*bubbleSort(arr))