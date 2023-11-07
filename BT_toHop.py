# way 2: DUNG CONG THUC PASCAL + DEQUY
# def ToHop(n, k): #2. tạo hàm ToHop(n,k)
#     if (k == 0) or (k == n): #3.1 check 2 nếu (k == 0) or (k == n) -> return 1
#         result = 1
#     else: #3.2 ngc lại
#         #3.2 cho biến result = dequy ToHop(n-1, k-1) + ToHop(n-1, k) || với n,k (4,2)
#             #3.2.1 tại n,k (4,2) dequy ToHop(n-1, k-1) -> n,k (3,1)
#                 #3.2.1.1 tại n,k (3,1) dequy ToHop(n-1, k-1) -> n,k (2,0) -> chạy if (k == 0) -> return 1
#                 #3.2.1.2 tại n,k (3,1) dequy ToHop(n-1, k)   -> n,k (2,1)
#                     #3.2.1.2.1 tại n,k (2,1) dequy ToHop(n-1, k-1) -> n,k (1,0) -> chạy if (k == 0) -> return 1
#                     #3.2.1.2.2 tại n,k (2,1) dequy ToHop(n-1, k)   -> n,k (1,1) -> chạy if (k == n) -> return 1
#                 #3.2.1.2 tại n,k (3,1) dequy ToHop(n-1, k) result => 2
#              #3.2.1 tại n,k (4,2) dequy ToHop(n-1, k-1) result => 3
#
#             #3.2.2 tại n,k (4,2) dequy ToHop(n-1, k) -> n,k (3,2)
#                 #3.2.2.1 tại n,k (3,2) dequy ToHop(n-1, k-1) -> n,k (2,1)
#                     #3.2.2.1.1 tại n,k (2,1) dequy ToHop(n-1, k-1) -> n,k (1,0) -> chạy if (k == 0) -> return 1
#                     #3.2.2.1.2 tại n,k (2,1) dequy ToHop(n-1, k)   -> n,k (1,1) -> chạy if (k == n) -> return 1
#                 #3.2.2.1 tại n,k (3,2) dequy ToHop(n-1, k-1) => result = 2
#                 #3.2.2.2 tại n,k (3,2) dequy ToHop(n-1, k)   -> n,k (2,2) -> chạy if (k == n) -> return 1
#             #3.2.2 tại n,k (4,2) dequy ToHop(n-1, k) => result = 3
#         #3.2 Từ #3.2.1 & #3.2.2 ⇒ result = tại n,k (4,2) dequy ToHop(n-1, k-1) + tại n,k (4,2) dequy ToHop(n-1, k)  = 3+3
#                               # ⇒ result = 6
#         result = ToHop(n-1, k-1) + ToHop(n-1, k)
#         print(result)
#     return result #3.3 return result
# print(ToHop(5,3)) #1. input n,k (4,2)  #4 print kqua

# # way 1: DÙNG DINH NGHIA + hàm tính giai thừa
# from functools import reduce
# # ham tính giai thua
# def factorial(n):
#     return reduce(lambda x, y: x*y, range(1, n+1))
#
# # print(factorial(5-9))
# n=6
# k=3
# toHop = factorial(n)//factorial(k)
# toHop = toHop//factorial(n-k)
# print(toHop)

# way 3: mảng 2 chiều
def ToHop(n, k):
    #1. tạo mảng 2c C với số col = k & số row = n , các phần tử =0
    C = [[0 for col in range(k+1)] for row in range(n+1)]
    # print(C)
    #2. cho các index 0 của các hàng = 1
    for i in range( 0 , n+1):
        C[i][0] = 1

    for j in range( 1 , k+1): #3.1 xài vòng lặp for bđ tại index 1 của col
        for i in range( j, n+1): #3.2. xài vòng lặp for bđ tại index 1 của row
            C[i][j] = C[i-1][j-1] + C[i-1][j] #3.2.1. ta cộng lại để tạo tamgiac pascal
    for e in C:
        print(e)
    return C[n][k] #4. trả phần tử tại index C[n][k]

print(ToHop(9, 6)) #5. truyền n,k vào hàm ToHop(n, k)


#way 4: dung mảng 1c
def ToHop(n, k):
    # 1. tạo mảng 1c A với số col = k+1 , các phần tử =0
    A = [0 for col in range(k + 2)]
    # print(A)
    A[0] = 1 #2. cho index_0 = 1
    print(A)
    for j in range(1, n+1): #3.1 chạy vòng lặp for để chạy lại mảng với n vòng
        for i in range(0, k+1): #3.2 chạy vòng lặp for để tạo tamgiac Pascal
            A[k-i] = A[k-i] + A[k-i-1]
            # print('k-i',k-i)
        print(A)
    return A[k] #4. trả phần tử tại index A[k]
print(ToHop(9,6)) #5. truyền n,k vào hàm ToHop(n, k)


# #way 5: dùng định nghĩa + dequy
# def ToHop(n, k): #2. tạo hàm ToHop(n,k)
#     if (k == 0): #3.1 check 2 nếu (k == 0) or (k == n) -> return 1
#         return 1
#     else: #3.2 ngc lại -> cho biến result = dequy ToHop(n-1, k-1) + ToHop(n-1, k) || với n,k (4,2)
#         return (n-k+1) * ToHop(n, k-1)//k
#
# print(ToHop(5,3)) #1. input n,k (4,2)

#way 6: dùng định nghĩa + for
def combination(n,k):
    result = 1
    for i in range(1,k+1):
        result = result*(n-i+1)//i
    return result
print(combination(9,6))