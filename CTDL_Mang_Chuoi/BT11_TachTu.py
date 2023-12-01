# #WAY 1:
# #1. input string
# # first_str_a = str(input())
# first_str_a = 'PhamThiHongDao'
# #2. khai báo chuỗi last_str_a = ''
# last_str_a = 'Ket qua tach tu:'
#
# #3. xài vòng lặp for lấy từng kí tự ở string ban đầu
# for i in first_str_a:
#     #3.1 xài hàm ord() trả về một số nguyên đại diện cho mã Unicode của ký tự được chỉ định.
#     ord_str_a = ord(i)
#     ''' Các ký tự từ 'A' đến 'Z' nằm ở vị trí từ 65 đến 90 trong bảng mã ASCII.
#     Các ký tự từ 'a' đến 'z' nằm ở vị trí từ 97 đến 122 trong bảng mã ASCII.'''
#     if 65 <= ord_str_a <= 90: #nêu là chữ in hoa thì thêm khoảng cách
#         last_str_a += " "
#     last_str_a += i.lower()
#
# print(last_str_a)


#--------------------------------------------------------------
#WAY 2:
#1. input string
# first_str_a = str(input())
first_str_a = 'PhamThiHongDao'
#2. khai báo chuỗi last_str_a = 'Ket qua tach tu:'
last_str_a = 'Ket qua tach tu:'
#3. xài vòng lặp for lấy từng kí tự ở string ban đầu
for i in first_str_a:
    if i.istitle(): #nêu là chữ in hoa thì thêm khoảng cách
        last_str_a += ' '
    last_str_a += i.lower()
print(last_str_a)