# Nhập vào một số nguyên dương n, tiếp theo là n số nguyên lần lượt là các phần tử trong dãy a.
#
# Hãy hoán đổi phần tử nhỏ nhất đầu tiền và phần tử lớn nhất cuối cùng trong dãy đó.
# In dãy sau khi hoán đổi ra màn hình, phía sau mỗi phần tử có đúng một khoảng trắng.

#WAY 1:
# #khai bao mang a
# # a = [int(input()) for i in range(int(input()))]
# a= [1,2,3,4]
#
# indexMin = a.index(min(a)) #tao bien indexMin = indexMin của mang a
# indexMax = 0 #tao indexMax = 0
# #xai for tìm indexMax cuối cùng
# for i in range(0,len(a)):
#     if a[indexMax]<= a[i] and indexMax < i:
#         indexMax=i
#
# valueMin = a[indexMin] #cho valueMin = phần tử ở indexMin của mảng a
# a.insert(indexMin,a[indexMax]) #them phan tu max cuôi vào indexMin của mảng a
# a.remove(a[indexMin+1]) #remove phần tử Min với index Min đầu tiên
#
# a.insert(indexMax,valueMin) #them valueMin vào indexMax của mảng a
# a.pop(indexMax+1) #xóa phần tử Max ở indexMax+1 của mảng a
# print(*a)


#WAY 2:
#khai bao mang a
# a = [int(input()) for i in range(int(input()))]
a= [1,2,3,4]

indexMin = a.index(min(a)) #tao bien indexMin = indexMin của mang a
indexMax = 0 #tao indexMax = 0
#xai for tìm indexMax cuối cùng
for i in range(0,len(a)):
    if a[indexMax]<= a[i] and indexMax < i:
        indexMax=i

temVal = a[indexMin] #tao temVal = phân tư min của mảng a
a[indexMin] = a[indexMax] # cho vị trí của index min = phần tử ở vtri indexMax
a[indexMax]  = temVal  # cho vị trí của index max = temVal

print(*a)