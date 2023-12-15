# Cho một số nguyên K.
# Tạo tất cả các chuỗi nhị phân có kích thước K sao cho nó không có chứa các số 1 liên tiếp cạnh nhau.
# Với k = 3 thì kết quả mong muốn là: "000 001 010 100 101 "

# #way1:
# def binary(k,s,lst):
#     if k == 0:#1. check nếu k=0 thì
#         if s not in lst: #1.1 check nếu s ko có trong lst thì append vào lst; return
#             lst.append(s)
#         return
#     # 2. ngc lại nếu k!=0 thì, xài vòng lặp for để lấy 0 & 1
#     for i in range(0,2):
#         if str('1') == s[len(s) - 1:]: #2.1 nếu cuối string s là '1'
#             binary(k-1,s+ str('0'),lst) #thì thêm 0 thay vì 1 vào string s -> continue
#             continue
#         # 2.2 nếu cuối string s ko phải 1 thì dequy hàm  binary(k-1,s+ str(i),lst) : thêm i vào string s
#         binary(k-1,s+ str(i),lst)
#
# k = int(input()) #1. input k
# lst = [] #2. khai báo mảng lst
# binary(k,'',lst) #3. chạy hàm binary(k,'',lst)
# #4. print theo yc đề bài
# for i in lst:
#   print(str(i),end=" ")


# #--------------------------------------
#way 2:
# Python3 program to Generate all binary string without consecutive 1's of size K

# A utility function generate all string without consecutive 1'sof size K
def generateAllStringsUtil(K, str, n):
    # print binary string without consecutive 1's
    if (n == K):
        # terminate binary string
        print(*str[:n], sep="", end=" ")
        return

    # if previous character is '1' then we put only 0 at end of string
    # example str = "01" then new string be "000"
    if (str[n - 1] == '1'):
        str[n] = '0'
        generateAllStringsUtil(K, str, n + 1)

    # if previous character is '0' than we put both '1' and '0' at end of string
    # example str = "00" then new string "001" and "000"
    if (str[n - 1] == '0'):
        str[n] = '0'
        generateAllStringsUtil(K, str, n + 1)
        str[n] = '1'
        generateAllStringsUtil(K, str, n + 1)


# function generate all binary string without consecutive 1's
def generateAllStrings(K):
    # Base case
    if (K <= 0):
        return

    # One by one stores every binary string of length K
    str = [0] * K

    # Generate all Binary string starts with '0'
    str[0] = '0'
    generateAllStringsUtil(K, str, 1)

    # Generate all Binary string starts with '1'
    str[0] = '1'
    generateAllStringsUtil(K, str, 1)


# Driver code
K = 3
generateAllStrings(K)

