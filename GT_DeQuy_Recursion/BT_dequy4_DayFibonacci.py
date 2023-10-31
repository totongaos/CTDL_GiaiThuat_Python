# Dãy số fibonacci là dãy số được tạo bằng cách như sau:
# Hai số đầu tiên là số 1.
# Các số tiếp theo lần lượt được tạo thành từ tổng của 2 số trước nó.
# Dãy fibonacci: 1, 1, 2, 3, 5, 8, 13, 21, ...
# Nhập vào một số nguyên dương n, hãy đưa ra số fibonacci thứ n. Hãy thực hiện điều đó bằng giải thuật đệ quy.


def fibonacci(n):
    if n==1 or n==2: return 1
    return fibonacci(n-1) + fibonacci(n-2)

# n = int(input())
n = 7
print(fibonacci(n))