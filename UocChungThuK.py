def CommonDiv(x,y,k):
    count = 0
    for i in range(2,x+1):
        if x%i==0 and y%i==0:
            count +=1
            if count == k:
                return i
    return -1
# x = int(input())
# y = int(input())
# k = int(input())
# print(CommonDiv(x,y,k))
print(CommonDiv(20,24,4))