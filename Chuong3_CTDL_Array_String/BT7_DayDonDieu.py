# Hãy kiểm tra xem dãy a có phải là dãy đơn điệu hay không, trả về "YES" nếu có, "NO" nếu không.
#
# Một dãy đơn điệu khi nó là dãy số tăng (a[i] > a[i-1]), hoặc dãy số giảm (a[i] < a[i-1]).

n = int(input())
arr=[int(x) for x in input().split()]

check1 = check2 = True
for i in range(1,n):
  if arr[i] >= arr[i-1]:
    check1 = False
  if arr[i] <= arr[i-1]:
    check2 = False
if check1 or check2: print("YES")
else: print("NO")