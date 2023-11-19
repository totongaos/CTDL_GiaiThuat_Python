# Hãy viết chương trình tính tổng của một dãy số gồm n số nguyên được nhập từ bàn phím.

# n = int(input())
n=3
arr = [int(x) for x in input().split()]

Sum = 0
for i in arr:
    Sum += i

print(Sum)