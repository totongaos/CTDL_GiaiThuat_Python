# Đầu vào gồm 2 số m và n tương ứng với số hàng và số cột của mạ trận.
# m dòng tiếp theo mỗi dòng là một hàng ma trận tương ứng với n phần tử

# HÀM INPUT TỪNG PHẦN TỬ TRONG 1 HÀNG
def matrix_lst_row(matrix_first,x,n_col):
    #1. khai báo 1 mảng lst_row chưá từng hàng của mảng chuyển vị
    lst_row = []
    #2. xài 2 vòng lặp for để lấy index của phần tử chuyển vị
    for row in range(0,len(matrix_first)):
        for col in range(x,len(matrix_first[row]),n_col):
            lst_row.append(matrix_first[row][col]) #3. append phần ử vào trong mảng
    return lst_row #4. return mảng
# print(matrixTransposition(matrix_first,m_row,n_col))

#1. input 2 biến m_row & n_col
# m_row, n_col = [int(x) for x in input().split()]
m_row = 4
n_col = 3
#2. khai báo & input mảng matrix_first
matrix_first = []
# matrix_first = [[0 for x in range(n_col)] for y in range(m_row)]
# for i in range(m_row):
#     matrix_first.append([i for i in input().split()])
matrix_first = [[1,3,0],
                [3,4,1],
                [5,6,2],
                [4,3,4],]
print(matrix_first)

#3. khai báo mảng lst_matrixTran
lst_matrixTran = []
#4. xài vòng lặp for append từng hàng vào mảng lst_matrixTran
for x in range(0,n_col):
    lst_matrixTran.append(matrix_lst_row(matrix_first,x,n_col))
print(lst_matrixTran)