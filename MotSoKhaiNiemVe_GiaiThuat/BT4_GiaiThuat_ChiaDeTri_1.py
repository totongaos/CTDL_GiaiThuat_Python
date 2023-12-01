'''
Cho một dãy gồm n số nguyên và một số nguyên x. Hãy đếm xem trong dãy có bao nhiêu phần tử có giá trị x.
'''
#Hàm chia để trị divide_and_conquer
def dynamic_programming(arr , x , L , R):
    if L == R:
        if arr[L] == x : return 1
        else: return 0
    else:
        mid = (L+R)//2
        return divide_and_conquer(arr , x , L , mid ) + divide_and_conquer( arr , x , mid + 1 , R)

#1. input n & mang arr
# n = int(input())
# arr = [int(input()) for i in range(n)]
# x = int(input())
n = 8
arr = [1,2,3,4,5,6,7,8]
x = 1
# #2. print kqua sử dung function divide_and_conquer đã viết ở trên
print(divide_and_conquer(arr , x , 0 , n-1))
