'''
Cho ma trận kề → chuyển sang DS kề tương ứng
'''
from collections import defaultdict
if __name__ == '__main__':
    n = int(input("nhap so luong dinh: "))
    a = [[0]*n for i in range(n)] #matrix ke cua dinh
    adj = defaultdict(list)  # graph luu DS ke cua dinh

    #Input matrix ke
    for i in range(0,n):
        a[i] = [int(z) for z in input().split()]

    #Tao ra DS Canh
    for i in range(n):
        for j in range(i,n): #range i-> n đe tranh lap canh
            if a[i][j]:
                adj[i].append(j+1)
                adj[j].append(i+1)

    # #In matran ke tuong ung adjacency_matrix
    for row in range(n):
        print(row+1,':',adj[row],end="\n")


'''
5
0 1 1 1 0
1 0 1 1 1
1 1 0 1 1
1 1 1 0 1
0 1 1 1 0
'''