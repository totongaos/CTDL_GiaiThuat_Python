# Nhập vào một số nguyên dương n, tiếp theo là n số nguyên lần lượt là các phần tử trong dãy a, cuối cùng nhập số nguyên x.
# Hãy đưa ra chỉ số đầu tiên của phần tử đầu tiên có giá trị bằng x, nếu không tồn tại số đó thì trả về -1.

# WAY 1:
# a = [int(input()) for i in range(int(input()))]
# x = int(input())
# def check_index(x):
#     for i in a:
#         if i == x:
#             return True
#
# if check_index(x):
#     print(a.index(x))
# else:
#     print(-1)

# WAY 2:
a = [int(input()) for i in range(int(input()))]
x = int(input())
for i in a:
    if i == x: print(a.index(x)); break
print(-1)