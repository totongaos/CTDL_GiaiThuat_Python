'''
**Kapsack Problem** là bài toán tên chộm mang theo 1 cái túi có dung lượng nhất định.
**Mục đích:** chất đồ vật sao cho tổng trọng lượng không vượt quá dung lượng của cái túi & tổng giá trị lấy được là lớn nhất
**Cụ thể:** Có n đồ vật `i` có trọng lượng `w_i` & giá trị `c_i` . Với i = 1,2,…,n
**Note** mỗi đồ vật chỉ lấy được 1 lần

Tìm cách chất các đồ vật này vào cái túi có dung lượng là `b`,
sao cho tổng trọng lượng của các đồ vật được chất vào túi là ko quá `b` & tổng giá trị lấy được là lớn nhất
**VÍ DỤ:** Cho 6 đồ vật (n=6), và túi có **trọng lượng b = 19.** Các đồ vật có trọng lượng & giá trị như sau:
'''

#1. khai báo biến fi && fo
fi = open('balo.inp')
fo = open('balo.out', 'w')
#2. đọc dòng đầu tiên của file balo.inp; gán cho 2 biến n && b
n,b = list(map(int,fi.readline().split()))
print(n,b)
#3. khi báo 2 mảng c && w và cho phần tử đầu tiên = 0
# -> de xet 2case căn bản [i,0] &&b[0,j]
c = [0]
w = [0]
print(c,w)
#4. xài vòng lặp for: đọc các dòng còn lại cuủa file balo.inp
for i in range(1,n+1):
    #4.1 gán cho 2 biến c_i && w_i
    c_i,w_i = list(map(int, fi.readline().split() ))
    #4.2 append 2 biến vaào mảng c && w
    c.append(c_i)
    w.append(w_i)
print(c,'\n',w)

#5. xài vòng lặp for khởi tạo bảng result mảng 2c | với b+1 col && n+1 row.
# Với phần tử = 0 -> de xet 2case căn bản [i,0] &&b[0,j]
result = [ [0]*(b+1) for i in range(n+1)]
# for x in range(n+1):
#     print(result[x])
#6. **(Cthuc Quy Hoach Dong)** tìm giá trị tối đa mang theo
for i_n in range(1,n+1):
    for L_b in range(1,b+1):
        result[i_n][L_b] = result[i_n - 1][L_b]
        if L_b >= w[i_n]:
            result[i_n][L_b] = max(result[i_n - 1][L_b] , result[i_n - 1][L_b - w[i_n]] + c[i_n])
print(result[n][b])
for x in range(n+1):
    print(result[x])

#7. truy vết vật mang theo (ko show tổng các vật trong balo)
i_n = n
L_b = b
lst_i_n = []
while i_n:
    if result[i_n][L_b] != result[i_n - 1][L_b]:
        lst_i_n.append(i_n)
        L_b = L_b - w[i_n]
    i_n -= 1
print(lst_i_n)