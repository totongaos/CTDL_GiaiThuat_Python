def dynamic_programming(arr,n):
    # 0. Cai thong bao loi
    if n == 0:
        return "0"
    # 0. Fix bug khi mang chi ci 1 phan tu
    elif n == 1:
        return f'{arr[0]}'

    #1. for khởi tạo bảng result mảng 2c | với n+1 col && 2 row.
    result = [[0,0]for i in range(n)]
    #1.1. 0-le 1-chan
    for i in range(0 , n):
        result[0][0] = 0
        result[0][1] = arr[0]

    #2. **(Cthuc Quy Hoach Dong)**
    for i in range(1, n):
        for j in range(0, i):
            if arr[i] == arr[j]:
                result[i][0] = max(result[j][1] +  arr[i] , result[i][0])
            else:
                result[i][1] = max(result[j][0] +  arr[i] , result[i][1])

    #3. truy vet
    max_res  = float('-inf')
    for i in result:
        max_res  = max(i[0],i[1],max_res)
    return f'{max_res}'

#1. input n & mang arr
n = 4
arr = [5,2,2,2]

#2. goi ham dynamic_programming(arr,n,money)
print(dynamic_programming(arr,n))