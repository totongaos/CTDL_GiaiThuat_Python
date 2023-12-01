#check 1 dãy số có phải cấp số cộng hay không?

n=int(input())
arr = [int(x) for x in input().split()]
temp1 = arr[1] - arr[0]
check = True
for i in range(1,n):
  temp = arr[i] - arr[i-1]
  if temp != temp1:
    check = False
    break
if check: print("YES")
else: print("NO")