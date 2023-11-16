'''Nhập vào hay số nguyên n và k (1 ≤ k ≤ n ≤ 9)
Hãy đưa ra tất cả những tổ hợp chập k của n, các chuỗi sắp xếp theo thứ tự tăng dần, sau một chuỗi có đúng một khoảng trắng.'''

# ----------------------------------------------------------
# way 1:
def combination(n,str_s,count,h): #3. tạo hàm combination(n,str_s,count,h)
    # 3 thêm count để xài for, nêu ko để count nó sẽ ko đủ số
    if n==0:
        print(str_s, end=" ")#4 in ra từng đoạn
    else:
        # chạy vòng lặp for -> lấy từng phần tử để tô hợp -> ta cho i = 1+h để liệt kê ra các tập hợp tăng dần
        for i in range(1+h,count+1):
            # print('str(i)',str(i))
            if str(i) in str_s: continue# Kiểm tra xem trong chuỗi đã có i chưa -> nếu chuỗi có i -> pass
            #nêu trong chuỗi có i -> xài đệ quy để add từng phần tử
            combination(n-1,str_s + str(i),count,h+1)
            h+=1
#B1. input count,k
# count = int(input())
# k = int(input())
count =5
k=3
h=0 #khai báo h
#gọi hàm combination(k,'',count,h)
combination(k,'',count,h)


