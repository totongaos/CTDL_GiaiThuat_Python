'''Cho dãy số nguyên a gồm n số nguyên.
Tìm dãy con dài nhất không giảm trong a, **dãy con liên tiếp + truy vết**
nếu có nhiều dãy con dài nhất thì chọn lần xuất hiện đầu tiên.'''

#---------------------------------------------
#way 1:
#Ham display, truy vết dãy con
def display(arr, l,r):
    #l = csMax - lst[csMax] + 1 | cong thuc đe tinh index của l
    #r = csMax | cong thuc đe tinh index của r
    print('dãy con dài nhất:',end=" ")
    for i in range(l,r+1):
        print(arr[i],end=" ")
#Ham dynamic_programming
def dynamic_programming(arr,n):
    #0. Cài thông báo lỗi
    if n == 0:
        print("Mảng rỗng nên ko có dãy con!!!")
        return
    #0. Fix bug khi mảng chỉ có 1 phần tử
    elif n == 1:
        print(arr[0],end=" ")
        return
    #1. lst luu tru cac đo dai cua day con
    lst =[0]*n
    lst[0] = 1
    for i in range(0,n):
        if arr[i] >= arr[i-1]:
            lst[i] = lst[i-1] + 1
        else:
            lst[i] = 1
    print('cac đo dai cua day con:',lst)
    #2. tim index cua phan tu lon nhat
    index_Max = lst.index(max(lst))
    #3. Goi ham display(arr, l,r)
    display(arr,index_Max - lst[index_Max] + 1,index_Max)
#1. input n & mang arr
# n = int(input())
# arr = [int(input()) for i in range(n)]
n = 2
arr = [2,3]
#2. chay ham dynamic_programming
dynamic_programming(arr,n)


# #---------------------------------------------
# #Way 2:
# # python3 - Codelearn cds_74: https://codelearn.io/learning/data-structure-and-algorithms/899135
#     # Tìm longest non decrease sub_array xuất hiện đầu tiên trong array dữ liệu n phần tử tên data
#     # Idea: Duyệt từng phần tử từ trái sang phải, so sánh từng cặp phần tửu liền kề từ trái sang phải,
# # cư phần tử phải lớn hơn hoặc bằng trái thì đếm thêm 1 và mảng chứa các phần tử là result
#
#     # Lưu các kết quả số đếm được vào một array tên long_count
#     # Tìm index của longest_count đầu tiên trong long_count, gán biến là longest_1st_idx
#     # Trả về kêt quả mảng cần tìm tên result = data [longest_1st_idx:]
#
# def long_count (data, l, r):
#     count = 0
#     for i in range (l+1, r+1):
#         if data[i] >= data [i-1]:
#             count += 1
#         else:
#             break
#     return count
#
# def longest_nonde (data):
#     r = len(data) - 1
#     long = []
#     for j in range (len(data)):
#         long.append(long_count (data, j , r))
#     longest_idx = 0
#     longest = long[longest_idx]
#     for i in range(len(long)-2):
#         if long[i+1] > longest:
#             longest_idx = i+1
#             longest = long[longest_idx]
#     result = [str(data[i]) for i in range(longest_idx, longest_idx+longest+1)]
#     return ' '.join(result)
#
# n = 7
# arr = [1, 2, 1, 4, 5, 6, 2]
# print(longest_nonde (arr))