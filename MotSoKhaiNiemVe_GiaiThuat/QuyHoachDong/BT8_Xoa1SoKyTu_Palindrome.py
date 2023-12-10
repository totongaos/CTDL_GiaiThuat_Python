'''
Một chuỗi s được gọi là đối xứng nếu khi viết ngược s lại thì s vẫn không thay đổi,
ví dụ "1221", "232" là chuỗi đối xứng, còn"123" không là chuỗi đối xứng.

Cho một chuỗi s, hãy xóa một số ký tự trong s để được một chuỗi đối xứng dài nhất.
Nếu có thể tạo được nhiều chuỗi đối xứng cùng độ dài thì đưa ra chuỗi đầu tiên.
'''


def palindrome(str_a,temp):
    n = len(str_a)
    m = len(temp)

    # 0. Cài thông báo lỗi
    if n == 0:
        return "Mảng rỗng nên ko có dãy con!!!"
    # 0. Fix bug khi mảng chỉ có 1 phần tử
    elif n == 1:
        return f'{str_a[0]}'

    #1. xai vong lap for khoi tao bang result mang 2c | voi n+1 col && m+1 row.
    result = [[0]*(n+1) for i in range(n+1)]
    #2. **(Cthuc Quy Hoach Dong)**
    for i in range(1, n):
        for j in range(1, m+1):
            if str_a[i-1] == temp[j-1]: #neu trung nhau -> tang len 1 dvi
                result[i][j] = result[i-1][j-1] +1
            else:
                aa = result[i - 1][j]
                a1a = result[i][j-1]
                result[i][j] = max(result[i - 1][j], result[i][j-1]) #neu 0 trung nhau -> lay value max

    '''for x in range(n):
        print(str_a[x] , result[x])
    print('-' * 20)
    0 a c s b b a a ->j
    0 [0, 0, 0, 0, 0, 0, 0, 0]
    a [0, 1, 1, 1, 1, 1, 1, 1]
    a [0, 1, 1, 1, 1, 1, 2, 2]
    b [0, 1, 1, 1, 2, 2, 2, 2]
    b [0, 1, 1, 1, 2, 3, 3, 3]
    s [0, 1, 1, 2, 2, 3, 3, 3]
    c [0, 1, 2, 2, 2, 3, 3, 3]
    a [0, 1, 2, 2, 2, 3, 4, 4]'''

    #3. TRUY VET
    lst = []
    i, j = m, n
    while i > 0 and j > 0:
        if str_a[i - 1] == temp[j - 1]: #Neu 2 ki tu giong nhau -> tra ve kq && di cheo lui lai
            lst.append(temp[j - 1])
            i -= 1
            j -= 1
        else:  #Neu khac nhau -> di len hoac xuong tuy theo huong nao co gia tri lon hon
            # print(result[i - 1][j] , result[i][j-1])
            if result[i - 1][j] < result[i][j-1]:
                j -= 1
            else:
                i -= 1
    return ''.join(lst)

#1. input string
# str_a = str(input())
str_a = '123a'
temp = str_a[::-1]  #dao ngc chuoi

# print(str_a,temp)

print(palindrome(str_a,temp))