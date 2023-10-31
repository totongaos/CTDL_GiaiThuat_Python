# Nhập vào một số nguyên n (1 ≤ n ≤ 9).
# Hãy đưa ra các chuỗi hoán vị của các số từ 1 đến n, các chuỗi tăng dần theo thứ tự từ điển, sau mỗi chuỗi hoán vị có đúng một khoảng trắng.

#way 1:
# n = int(input())
# n=3
# arr=[]
# def permutation(n, s):
#     global arr
#     if n == 0:
#         print(s, end=" ")
#     else:
#         for i in range(1,n+1):
#             if str(i) in s: continue
#             # if str(i) in arr: continue
#             # arr.append(str(i))
#             permutation(n-1, s+str(i))
#             # permutation(n - 1, s + str(i))
#             # print(s)
#             # s += str(i)
#
# permutation(n,"")
# print(arr)


#way 2:
def hoan_vi(lst):
    if len(lst) == 1:
        return [lst]
    result = []
    for i in range(len(lst)):
        m = lst[i]
        rest = lst[:i] + lst[i + 1:]

        for x in hoan_vi(rest):
            p = [m] + x
            result.append(p)
    return result
n = 4
lst = [i for i in range(1, n + 1)]
result = hoan_vi(lst)
print(result)

if result:
    for x in result:
        for p in x:
            print(str(p), end='')
        print(end=' ')




#way :
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(curr):
            if len(curr) == len(nums):
                ans.append(curr[:])
                return

            for num in nums:
                if num not in curr:
                    curr.append(num)
                    backtrack(curr)
                    curr.pop()

        ans = []
        backtrack([])
        return ans