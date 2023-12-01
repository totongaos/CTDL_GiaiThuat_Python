# Hãy in lần lượt các số Narcissistic có trong dãy a ra màn hình, sau mỗi phần tử có đúng một khoảng trắng.
# Nếu không có phần tử nào thỏa mãn thì in "NO".

def check_narcissistic(x):
    x = str(x)
    result = 0
    for i in range(len(x)):
        result += int(x[i])**len(x)
    if result == int(x):
        return True
    else:
        return False
n =2
arr = [1583,828]
# n = int(input())
# arr=[int(x) for x in input().split()]
check = True
for i in arr:
    if check_narcissistic(i):
        print(i, end=" ")
        check = False
if check:
    print("NO")


# #------------------------------------------------------------
# #way 2:
# def countDigit(n):
#     if (n == 0):
#         return 0
#     return (1 + countDigit(n // 10))
#
# # Returns true if n is Narcissistic number
# def check(n):
#     # Count the number of digits
#     l = countDigit(n)
#     dup = n;
#     sm = 0
#
#     # Calculates the sum of digits
#     # raised to power
#     while (dup):
#         sm = sm + pow(dup % 10, l)
#         dup = dup // 10
#
#     return (n == sm)
#
# n = int(input())
# a=[int(x) for x in input().split()]
# checkk = 0
# for i in range (0,n):
#     if (check(a[i])):
#         print(a[i],end=" ")
#         checkk = 1
#
# if checkk == 0 : print("NO")
#
# # This code is contributed by Nikita Tiwari.