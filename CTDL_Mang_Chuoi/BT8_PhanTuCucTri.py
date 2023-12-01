'''Trong toán học, phần tử cực trị (đỉnh) là các phần tử có giá trị không nhỏ hơn các lân cận của nó.
Cho một mảng arr[] gồm các giá trị số nguyên, hãy viết chương trình in ra chỉ số của các phần tử đỉnh trong mảng.
'''

n =2
arr = [-50,-50]
# n = int(input())
# arr=[int(x) for x in input().split()]

if n==1:
    print(0, end=" ")
else:
    if arr[0] >= arr[1]:
        print(0, end=" ")
    for i in range(1,n-1):
        if arr[i+1] <= arr[i] >= arr[i-1]:
            print(i, end=" ")
    if arr[n - 1] >= arr[n - 2]:
        print(n-1, end=" ")


