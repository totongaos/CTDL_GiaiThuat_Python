'''
Tìm số đồng tiền đổi được là ít nhất (cho túi tiền đỡ nặng)
'''
#--------------------------------------------------------
#way1
#HAM dynamic_programming
def dynamic_programming(arr,n):
    # 0. Cài thông báo lỗi
    if n == 0:
        return "Mảng rỗng nên ko có dãy con!!!"
    # 0. Fix bug khi mảng chỉ có 1 phần tử
    elif n == 1:
        return f'{arr[0] }'

    #1. xài vòng lặp for khởi tạo bảng result mảng 2c | với n+1 col && 2 row.
    result = [[0,0]for i in range(n)]
    #1.1. 0-le 1-chan
    for i in range(0 , n):
        # result[0][0] = 0
        result[0][1] = arr[0]

    for x in range(n):
        print(result[x],arr[x])
    print('-' * 20)

    #2. **(Cthuc Quy Hoach Dong)** tìm giá trị tối đa mang theo
    for i in range(1, n):
        for j in range(0, i): # j < i, j chạy từ 0 đến i)
            if arr[i] == arr[j]:
                result[i][0] = max(result[j][1] +  arr[i] , result[i][0])
            else:
                result[i][1] = max(result[j][0] +  arr[i] , result[i][1])

    for x in range(n):
        print(result[x],arr[x])

    #3. truy vet tổng giá trị lớn nhất của các phần quà mà Hải có thể chọn.
    max_res  = float('-inf')
    for i in result:
        max_res  = max(i[0],i[1],max_res)
    return f'max_a: {max_res }'

#1. input n & mang arr
# n = int(input())
# arr = [int(input()) for i in range(n)]
n =5
arr = [5,7,4,2,4]

#2. goi ham dynamic_programming(arr,n,money)
print(dynamic_programming(arr,n))
