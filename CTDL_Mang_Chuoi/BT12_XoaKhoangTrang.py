# --------------------------------------------------------------
#WAY 1: dùng leẹnh có sẵn trong python
#1. input string
# first_str_a = str(input())
first_str_a = ' Pham  Thi Hong   Dao '
#2. khai báo chuỗi last_str_a = ''
last_str_a = ''
# #3. print theo yc đề bài
first_str_a = first_str_a.split()
last_str_a = " ".join(first_str_a)
print(last_str_a)

