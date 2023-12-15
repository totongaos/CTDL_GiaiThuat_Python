# Với một ma trận 9x9. Mỗi ô có một giá trị từ '1' đến '9' hoặc viết bởi '.' tức là ô đó là khoảng trống.
# Hãy kiểm tra xem nếu đây là một câu đố Sudoku hợp lệ trả kết quả TRUE. Còn không phải là FALSE.
# Hàm set() No duplicate members. nên sẽ so sánh list với set để check có trùng num ko?


#1. input mảng 2c
# sudoku = []
# for i in range(9):
#     sudoku.append([i for i in input().split()])
sudoku = [['.', '1', '.', '.', '4', '.', '.', '2', '.'],
          ['.', '.', '6', '1', '.', '.', '.', '.', '.'],
          ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
          ['.', '.', '1', '.', '.', '.', '.', '.', '.'],
          ['.', '6', '7', '.', '.', '.', '.', '.', '9'],
          ['.', '.', '.', '.', '.', '.', '8', '1', '.'],
          ['.', '3', '.', '.', '.', '.', '.', '.', '6'],
          ['.', '1', '.', '.', '.', '7', '.', '.', '.'],
          ['.', '.', '.', '5', '.', '.', '.', '7', '.']]
# print(sudoku)

#HÀM CHECK 3X3:
def check_3x3(sudoku):
    #1. xài 2 vòng lặp for để lấy từng index của mảng
    for row in range(0,9,3):
        for col in range(0,9,3):
            lst_temp = [] #2. khai báo mảng tạm
            #3. xài 2 vòng lặp để gọi từng index 3x3
            for i in range(row,row+3):
                for j in range(col,col+3):
                    if sudoku[i][j].isnumeric():
                        lst_temp.append(sudoku[i][j])
            if len(lst_temp) != len(set(lst_temp)):
                return False
    return True
print(check_3x3(sudoku))

def check_col(sudoku):
    lst_temp = []
    for row in range(9):
        for col in range(9):
            if sudoku[row][col].isnumeric():
                lst_temp.append(sudoku[row][col])
        if len(lst_temp) != len(set(lst_temp)):
            return False
    return True
print(check_col(sudoku))



def check_row(sudoku):
    for row in sudoku:
        lst_temp = []
        for index_in_row in row:
            if index_in_row.isnumeric():
                lst_temp.append(index_in_row)
        if len(lst_temp) != len(set(lst_temp)):
            return False
    return True
print(check_row(sudoku))

if check_col(sudoku) and check_row(sudoku) and check_3x3(sudoku):
    print('TRUE')
else:
    print('FALSE')