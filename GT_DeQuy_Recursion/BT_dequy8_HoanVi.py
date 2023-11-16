# Nhập vào một số nguyên n (1 ≤ n ≤ 9).
# Hãy đưa ra các chuỗi hoán vị của các số từ 1 đến n, các chuỗi tăng dần theo thứ tự từ điển, sau mỗi chuỗi hoán vị có đúng một khoảng trắng.


# # way 1:
# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         def backtrack(curr):
#             if len(curr) == len(nums):
#                 ans.append(curr[:])
#                 return
#
#             for num in nums:
#                 if num not in curr:
#                     curr.append(num)
#                     backtrack(curr)
#                     curr.pop()
#
#         ans = []
#         backtrack([])
#         return ans
#     print(ans)


# ------------------------------------------------------
# # way 2:
# #2. tạo hàm permutation(arr) → hoán vị các phần tử của arr
# def permutation(arr):
#
#     if len(arr)==1:  #kiểm tra len(arr) == 1 → nếu bằng → ko cần hoán vị -> return [arr]
#         return [arr] #lưu ý chỗ này phải là [] -> dể khi n=1 ko bị lỗi => B6.1 ko phải thêm [] -> kqua mới sẽ ko bị dính mảng
#
#     final_arr =[] #4. tạo 1 list rỗng final_arr =[] để chứa các phần tử hoán vị của arr
#
#     for i in range(len(arr)): #5. dùng hàm for lấy từng index i trong arr
#         temp_arr = arr[i] #5.1. tạo biến temp_arr chưa phần tử ở vị trí i của mảng arr
#         rest_arr = arr[:i] + arr[i +1:] #5.2 tạo mảng rest_arr chưa các phần tử của mảng arr trừ phần tử ở vị trí i
#         print('temp_arr, rest_arr',temp_arr,rest_arr)
#         #6. dùng hàm for chạy đệ quy - quay lùi -> tạo biến temp_arr, mảng  rest_arr của mảng rest_arr
#         for x in permutation(rest_arr):
#         # for x in rest_arr:
#             child_arr = [temp_arr] + x #6.1 tạo biến child_arr = mảng chứa temp_arr + x (x: sẽ là từng phần tử của mảng arr đã tách ra khi dequy)
#             # print(child_arr)
#             final_arr.append(child_arr) #6.2 add biến child_arr vào mảng final_arr -> tý return mảng
#             # print(final_arr)
#
#     return final_arr #7. return mảng final_arr
#
# # n = int(input())
# n=3
# #1. tạo 1 array arr với các phần tử từ 1 đến n
# arr=[i for i in range(1,n+1)]
# # print(arr)
#
# #8. print ra theo yêu cầu đề
# result1 = permutation(arr)
# for child_arr in result1:
#     for i in child_arr:
#         print(i, end="")
#     print(end=" ")


# ----------------------------------------------------------
# way 3:
def permutation(n,str_s,count): #3. tạo hàm permutation(n,str_s,count)
    #3 thêm count để xài for, nêu ko để count nó sẽ ko đủ số
    if n==0: #4 in ra từng đoạn
        print(str_s, end=" ")
    else:
        #chạy vòng lặp for -> lấy từng phần tử để hoán vị
        for i in range(1,count+1):
            # print('str(i)',str(i))
            if str(i) in str_s: continue # Kiểm tra xem trong chuỗi đã có i chưa -> nếu chuỗi có i -> pass
            #nêu trong chuỗi có i -> xài đệ quy để add từng phần tử
            permutation(n-1,str_s + str(i),count)

#B1. input n
# n = int(input())
n =3
#2. gọi hàm permutation(n,'',n)
permutation(n,'',n)

