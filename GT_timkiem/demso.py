# Nhập và số nguyên dương n, tiếp theo là n số nguyên lần lượt là các phần tử trong dãy a, cuối cùng là nhập số nguyên x,
# hãy đếm xem trong dãy a có bao nhiêu phần tử có giá trị bằng x. In ra số đó.

a = [1,2,3,4,1]
x = 1
print(a.count(x))

# n = int(input())
# a = [int(input()) for i in range(n)]


# arr = [3,4,4,6,7,8,9,10,12,13]
# x = 10
# n =10
#
# L = 0
# R = n-1
# def interpolationSearch(L,R,arr,x):
#     while arr[L] != arr[R] and x >= arr[L] and x <= arr[R]:
#         mid = L + (R-L)*(x-arr[L])//(arr[R]-arr[L])
#         print((R-L)*(x-arr[L])//(arr[R]-arr[L]))
#         print(mid)
#         if arr[mid] < x:
#             L = mid+1
#         elif arr[mid] > x:
#             R = mid -1
#         else:
#             return print(mid)
#
# interpolationSearch(L,R,arr,x)
# print(arr[7])