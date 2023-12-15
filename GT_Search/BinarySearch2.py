# Cho số nguyên dương n, tiếp theo là n số nguyên dương của một dãy a, cuối cùng là một số s.
# Hãy đưa ra dãy con liên tiếp đầu tiên của dãy a sao cho tổng của dãy đó bằng s. In dãy đó ra màn hình,
# sau mỗi phần tử có một khoảng trắng. Nếu không tồn tại dãy đó thì in ra "-1".



# n = int(input())
# a = [int(input()) for i in range(n)]
# x = int(input())
# a = [1,2,3,8,5,6,7,9,15]
# x = 17
#
# n=int(input())
# arr=[int(input()) for _ in range (n)]
# x=int(input())
n =9
arr = [1,2,3,8,5,6,7,9,15]
x=7
new_arr=[0]*(n+1)
check=False
for i in range (n):
    new_arr[i+1]+=arr[i]+new_arr[i]
for i in range (1,n+1):
    if new_arr[i]>=x:
        compare=new_arr[i]-x
        l=0;r=i
        m=(l+r)//2
        while l<r:
            if new_arr[m]<compare:
                l=m+1
            else:
                r=m
            m=(l+r)//2
            if new_arr[m]==compare:
                end=i;start=m
                check=True
                break
    if check:
        print(*arr[start:end])
        break
else: print(-1)


# WAY 5
# def solve(a, s):
#     res = []
#     total = 0
#     i = 0;
#     while i < len(a):
#         if total < s:
#             total += a[i]
#             res.append(a[i])
#         elif total > s:
#             total -= res.pop(0)
#             i -= 1
#         else:
#             break
#         i += 1
#     return res if total == s else -1
# a = [1,2,3,8,5,6,7,9,15]
# s = 13
# res = solve(a, s)
# if type(res) == list:
#     print(" ".join([str(i) for i in res]))
# else:
#     print(-1)



#way 4: vuot qua 7 test case ve time chay
# n = int(input())
# a = [int(input()) for i in range(n)]
# x = int(input())
#
# lst = []
# def Sum_lst(a,x,lst):
#     for j in range(0,len(a)):
#         lst.clear()
#         S=0
#         i=0+j
#         while S<=x and i<len(a):
#             S += a[i]
#             lst.append(a[i])
#             if S == x:
#                 print(*lst)
#                 return lst
#             i += 1
#     return print(-1)
# Sum_lst(a,x,lst)


#WAY 2: HOI CHAM
# lst = []
# S=0
# def Sum_lst(a,x,lst,S):
#     for j in range(0,len(a)):
#         for i in range(0+j,len(a)):
#             S += a[i]
#             lst.append(a[i])
#             if S > x:
#                 lst.clear()
#                 S=0
#                 break
#             elif S == x:
#                 return lst
#     return -1
# print(*Sum_lst(a,x,lst,S))

#WAY 1:
# n = int(input())
# a = [int(input()) for i in range(n)]
# x = int(input())
#
# lst = []
# S=0
# def Sum_lst(a,x,lst,S):
#     for j in range(0,len(a)):
#         for i in range(0+j,len(a)):
#             if a[i] > x:
#                 S += a[i]
#                 lst.append(a[i])
#                 if S > x:
#                     lst.clear()
#                     S=0
#                     break
#                 elif S == x:
#                     return lst
#             else:
#                 lst.clear()
#                     S=0
#                     break
#     return -1
# print(*Sum_lst(a,x,lst,S))

# WAY 3:
# n = int(input())
# a = [int(input()) for i in range(n)]
# x = int(input())
#
# lst = []
#
# def Sum_lst(a,x,lst):
#     for j in range(0,len(a)):
#         lst.clear()
#         S=0
#         for i in range(0+j,len(a)):
#             if a[i] < x:
#                 S += a[i]
#                 lst.append(a[i])
#                 if S > x:
#                     break
#                 elif S == x:
#                     print(*lst)
#                     return lst
#             else:
#                 break
#     return print(-1)
# Sum_lst(a,x,lst)


n = int(input())
a = [int(input()) for i in range(n)]
x = int(input())
lst = []


def Sum_lst(a, x, lst):
    for j in range(0, len(a)):
        lst.clear()
        S = 0
        i = 0 + j

        while S <= x and i < len(a):
            S += a[i]
            lst.append(a[i])

            if S == x:
                print(*lst)
                return lst
            i += 1

    return print(-1)


Sum_lst(a, x, lst)