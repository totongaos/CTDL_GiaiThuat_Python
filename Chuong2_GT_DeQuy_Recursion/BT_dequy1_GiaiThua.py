# Nhập vào một số tự nhiện n (n ≤ 20).
# Hãy phương pháp đệ quy tìm và in ra giá trị của n!.
# (n! = 1 * 2 * 3 * ... * n). Quy ước 0! = 1.

n=3
# n = int(input())

def factorials(n):
    if n <= 1:
      return 1
    else:
      return n*factorials(n-1)

print(factorials(n))