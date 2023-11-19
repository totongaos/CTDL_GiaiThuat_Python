dic_Affine1 = {0:'a', 1:'b', 2:'c', 3:'d', 4:'e',
              5:'f', 6:'g', 7:'h', 8:'i', 9:'j',
              10:'k', 11:'l', 12:'m', 13:'n', 14:'o',
              15:'p', 16:'q', 17:'r', 18:'s', 19:'t',
              20:'u', 21:'v', 22:'w', 23:'x', 24:'y', 25:'z',}

'''dic_Affine = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4,
              'f':5, 'g':6, 'h':7, 'i':8, 'j':9,
              'k':10, 'l':11, 'm':12, 'n':13, 'o':14,
              'p':15, 'q':16, 'r':17, 's':18, 't':19,
              'u':20, 'v':21, 'w':22, 'x':23, 'y':24, 'z':25,}'''


#Hàm mã hóa
def encode(str_a, a, b, dic_Affine1, size_m):
    #1. khai báo string mã hóa rỗng: str_encode = ''
    str_encode = ''
    for s in str_a: #2. xài vòng lặp for lấy từng kí tự trong chuỗi cần đc mã hóa
        for x, value in dic_Affine1.items(): #2.1. xài vòng lặp for check kí tự mã hóa trong dict
            if s == " ": #2.1.1 thêm khoảng cách cho chuỗi mã hóa
                str_encode += " "
                break
            elif value == s.lower(): #2.1.2 mã hóa chuỗi
                y = (a * x + b) % size_m
                str_encode += dic_Affine1[y]
                break
    return str_encode #3. return chỗi đã mã hóa xong


#Hàm tìm số nghịch đảo
def find_inverse_num(a, size_m):
    #1. khai báo a nghịch đảo: a_1 = 1
    a_1 = 1
    while (a*a_1)%size_m != 1 and a_1<size_m: #2. dùng thuật toán Brute-force để tìm a_1
        a_1 += 1
    return a_1

#Hàm giải mã
def decode(str_encode,a_1,b,dic_Affine1):
    #1. khai báo string giải mã rỗng: str_decode = ''
    str_decode = ''
    for s in str_encode: #2. xài vòng lặp for lấy từng kí tự trong chuỗi cần đc giải mã
        for y, value in dic_Affine1.items(): #2.1. xài vòng lặp for check kí tự mã hóa trong dict
            if s == " ": #2.1.1 thêm khoảng cách cho chuỗi giải mã
                str_decode += " "
                break
            elif value == s.lower(): #2.1.2 giải mã chuỗi
                x = (a_1 * (y - b)) % 26
                str_decode += dic_Affine1[x]
                break
    return str_decode #3. return chỗi đã mã hóa xong

a=7
b=3
str_a = 'It is nice today'
#1. input khóa key{a,b}
# a ,b = [int(i) for i input().split()]
#2. input string mã hóa
# str_a = str(input())
size_m = len(dic_Affine1)

#3. chạy hàm mã hóa
str_encode=encode(str_a, a, b, dic_Affine1, size_m)
print('Encrypted Message is : ',str_encode)

#4. chạy hàm tìm số nghịch của a (a^-1)
a_1 = find_inverse_num(a, size_m)

#5. chạy hàm giải mã
str_decode = decode(str_encode,a_1,b,dic_Affine1)

#6. print theo yc đề bài
if str_a.lower() == str_decode.lower():
    print('Decrypted Message is : ',str_decode)
else:
    print('Cannot Encrypted and Decrypted this Message')