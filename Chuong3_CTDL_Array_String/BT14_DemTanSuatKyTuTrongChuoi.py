#Hàm đếm số lần xuất hiện
def countFrequency(a,str_a):
    count = 0
    for i in str_a:
        if a == i:
            count+=1
    return count

#1. input string
# str_a = str(input())
str_a = 'learningalgorithmwithtek4'
#2. khai báo mảng lst
lst = []
#3. xài vòng lặp for để lưu ký tự vào mảng lst để print
for i in str_a:
    if i not in lst:
        lst.append(i)
#4. xài vòng lặp for để print theo yc đề bài
for i in lst:
    print(f'{i}{countFrequency(i,str_a)}', end=" ")

