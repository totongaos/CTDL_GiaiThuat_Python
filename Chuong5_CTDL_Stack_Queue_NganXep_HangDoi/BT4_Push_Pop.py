print(3%2)
n,k=map(int,input().split())
arr=[int(x) for x in input().split()]

if k==n or (n==1 and k%2==1):
    print(-1)
elif k>n:
    print(max(arr))
else:
    t=-1
    for i in range(0,k-1):
        t=max(t,arr[i])
    ans=max(t,arr[k])
    print(ans)