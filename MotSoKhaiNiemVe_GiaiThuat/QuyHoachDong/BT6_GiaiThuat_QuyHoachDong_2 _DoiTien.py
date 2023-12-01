'''
Một ngân hàng có rất nhiều tiền với nhiều mệnh giá khác nhau, số lượng tờ tiền của mỗi mệnh giá được coi là nhiều vô kể.
Cho mảng a chứa các phần tử [a0, a1, a2 ..]. Đây là các mệnh giá tiền mà ngân hàng đang có.
Một người đến ngân hàng rút một số tiền x đồng, người đó muốn nhận số tiền đó với số tiền ít nhất.

Tính số tiền tối thiểu mà ngân hàng phải giữ để tổng giá trị của chúng là n đồng. Nếu không có cách nào để thay đổi, hãy trả về 0.
'''
#--------------------------------------------------------
#way1
def dynamic_programming(arr,n,money):
    #1. xai vong lap for khoi tao bang result mang 2c | voi b+1 col && n+1 row.
    # Với phần tử = 0 -> de xet 2case căn bản [i,0] &&b[0,j]
    result = [ [0]*(money+1) for i in range(n+1)]
    for x in range(1,money+1):
        result[0][x]=float('inf')

    #2. **(Cthuc Quy Hoach Dong)** Tim so đong tien doi ḍc la it nhat (cho tui tie do nạng)
    for i_n in range(1,n+1):
        for L_b in range(1,money+1):
            result[i_n][L_b] = result[i_n - 1][L_b]
            if L_b >= arr[i_n]:
                result[i_n][L_b] = min(result[i_n - 1][L_b] , result[i_n][L_b - arr[i_n]] + 1)

    if result[n][money] == float('inf'):
        return 'Tôi ko đủ tiền để đổi'
    else:
        return result[n][money]
    # for x in range(n+1):
    #     print(result[x])


#1. input n & mang arr
# n = int(input())
# arr = [0]
# for i in range(n):
#     arr.append(int(input()))
# money = int(input())
n = 5
arr = [0,2,4,6,8,10]
money = 8
#2. goi ham dynamic_programming(arr,n,money)
print(dynamic_programming(arr,n,money))
