# Hải vừa nghĩ ra một phép biến đổi số, cụ thể như sau:
#
# Với số tự nhiên n nếu:
# n là số chẵn thì biến đổi n thành n/2.
# n là số lẽ thì biến đổi n thành 3*n+1.
# Hiện tại Hải đang có hai số tự nhiên n và k, Hải muốn biết số lượng số mà khi số đó biến đổi k lần liên tiếp thì biến đổi thành số n.

# n=int(input())
# k=int(input())
n=5
k=2

def convert(n,k):
    global count
    if k == 0:
        return 1
    if (n - 1) % 3 == 0 and ((n - 1) // 3) % 2 == 1:
        return convert(2 * n, k - 1) + convert((n - 1) // 3, k - 1)
    return convert(2 * n, k - 1)

print(convert(n,k))
