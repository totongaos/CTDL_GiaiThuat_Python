# Cho số nguyên dương n, tiếp theo là n số nguyên cũng một dãy a, cuối cùng là một số x, biết dãy là dãy không giảm.
# Hãy đưa ra chỉ số của phần tử đầu tiên có giá trị bằng x, nếu không tồn tại giá trị đó đưa ra -1.



# n = int(input())
# a = [int(input()) for i in range(n)]
# x = int(input())
a = [1,2,3,4,5,6,7,9,15]
x = 4
n=9

# WAY 1:
# for i in range(0,len(a)):
#     if a[i] == x: print(i);break
# print(-1)

# WAY 2:
L = 0
R = n-1
def BinarySearch(a,x,L,R):
    while L < R:
        mid_idx = (R + L) // 2
        mid = a[mid_idx]
        if x>mid:
            L = mid_idx + 1
        else:
            R = mid_idx
    if a[L]==x:
        return L
    else:
        return -1
print(BinarySearch(a,x,L,R))

# WAY 3:
# a = [int(input()) for _ in range(int(input()))]
# try:
#     print(a.index(int(input())))
# except:
#     print(-1)