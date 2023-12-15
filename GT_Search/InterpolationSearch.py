# Nhập vào một số nguyên dương n, tiếp theo là n số nguyên lần lượt là các phần tử trong dãy a, cuối cùng nhập số nguyên x.
# Hãy đưa ra index đầu tiên có giá trị bằng x, nếu không tồn tại số đó thì trả về -1.

# n = int(input())
# a = [int(input()) for i in range(n)]
# x = int(input())

arr = [3,4,4,6,7,8,9,10,12,13]
x = 13
n =10

L = 0
R = n-1

#WAY 2: XÀI ĐỆ QUY
# def interpolationSearch(L,R,arr,x):
#     if L<=R and x >= arr[L] and x <= arr[R]:
#         mid = L + (R-L)*(x-arr[L])//(arr[R]-arr[L])
#         if arr[mid] == x: return mid
#         elif arr[mid] < x: return interpolationSearch(mid+1,R,arr,x)
#         elif arr[mid] > x: return interpolationSearch(L,mid-1,arr,x)
#     return -1
#
# print(interpolationSearch(L,R,arr,x))


# WAY 1:
def interpolationSearch(L,R,arr,x):
    while arr[L] != arr[R] and x >= arr[L] and x <= arr[R]:
        mid = L + (R-L)*(x-arr[L])//(arr[R]-arr[L])
        if arr[mid] < x:
            L = mid+1
        elif arr[mid] > x:
            R = mid -1
        else:
            return mid
    if arr[L] == x:
        return L
    else:
        return -1

print(interpolationSearch(L,R,arr,x))