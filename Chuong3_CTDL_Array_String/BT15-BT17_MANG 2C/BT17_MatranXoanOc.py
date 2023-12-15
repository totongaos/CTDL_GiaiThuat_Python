# Cho ma trận xoắn ốc là ma trận vuông kích thước N.
# Hãy viết chương trình cho phép in ra ma trận xoắn ốc với giá trị N được nhập vào từ bàn phím.

#1. input biến num
# num = int(input())
num = 5
#2. khai báo mảng spiralMatrix với num*num
spiralMatrix =[[0 for x in range(num)] for y in range(num)]
#3. khai báo các biến row, col, count -> lấy index -> add phần tử vào đúng index của mảng xoắn ốc
row = 0
col = num-1
count = 1

#4. xài vòng lặp for để input phần tử vào đúng index của mảng xoắn ốc
for i in range(0,num//2+1):
    #4.1. input hàng đầu
    for index_row in range(row,col+1):
        spiralMatrix[row][index_row] = count
        count += 1
    #4.2. input cột cuối
    for index_col in range(row+1,col+1):
        spiralMatrix[index_col][col] = count
        count += 1
    #4.3. input hàng cuối
    for index_row in reversed(range(row,col)):
        spiralMatrix[col][index_row] = count
        count += 1
    #4.4. input cột đầu
    for index_col in reversed(range(row+1,col)):
        spiralMatrix[index_col][row] = count
        count += 1
    row += 1
    col -= 1
# print(spiralMatrix)

#5. print ra theo yc đề bài
for i in range(0,num):
    for j in range(0,num):
        print(spiralMatrix[i][j], end=" ")
    print("", end="\n")

