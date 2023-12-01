'''
Tìm số đồng tiền đổi được là ít nhất (cho túi tiền đỡ nặng)
'''
#--------------------------------------------------------
#way1
def dynamic_programming(arr,n,money):
    #1. xai vong lap for khoi tao bang result mang 2c | voi b+1 col && n+1 row.
    # Với phần tử = 0 -> de xet 2case căn bản [i,0] &&b[0,j]
    result = [ [0]*(money+1) for i in range(n+1)]
    for x in range(1,money+1):
        result[0][x]=float('inf')
    print(result)
    #2. **(Cthuc Quy Hoach Dong)** Tim so đong tien doi ḍc la it nhat (cho tui tie do nạng)
    for i_n in range(1,n+1):
        for L_b in range(1,money+1):
            result[i_n][L_b] = result[i_n - 1][L_b]
            if L_b >= arr[i_n]:
                result[i_n][L_b] = max(result[i_n - 1][L_b] , result[i_n-1][L_b - arr[i_n]])
    #3. check có đủ tiền để đổi ko
    if result[n][money] == float('inf'):
        return 'Tôi ko đủ tiền để đổi'
    else:
        return result[n][money]

#1. input n & mang arr
# n = int(input())
# arr = [0]
# for i in range(n):
#     arr.append(int(input()))
# money = int(input())
money = 5
arr = [0 , 10, 6, 7, 6, 1]
n = 2
#2. goi ham dynamic_programming(arr,n,money)
print(dynamic_programming(arr,n,money))
