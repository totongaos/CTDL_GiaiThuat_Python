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


#-----------------------------------------------------------------------------------------
def fib(n):
    if n == 1 or n == 0:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
print(fib(5))

'''
1. tại n=5 -> fib(n-1) = fib(4) 
    1.1 tại fib(4) -> fib (n-1) = fib(3)
        1.2 tại fib(3) -> fib(n-1) = fib(2)
            1.3 tại fib(2) -> fib(n-1) = fib(1) -> return 1
            1.3 tại fib(2) -> fib(n-2) = fib(0) -> return 1
        1.2 tại fib(3) -> fib(n-2) = fib(1) -> return 1

    1.1 tại fib(4) -> fib (n-2) = fib(2)
        1.2 tại fib(2) -> fib(n-1) = fib(1) -> return 1
        1.2 tại fib(2) -> fib(n-2) = fib(0) -> return 1

2. tại n=5 -> fib(n-2) = fib(3)
    2.1 tại fib(3) -> fib(n-1) = fib(2)
        2.2 tại fib(2) -> fib(n-1) = fib(1) -> return 1
        2.2 tại fib(2) -> fib(n-2) = fib(0) -> return 1
    2.1 tại fib(3) -> fib(n-2) = fib(1) -> return 1
=> ta cộng dồn các return lại với nhau sẽ đc kquả
'''