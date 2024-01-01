'''
Cho ma trận kề → chuyển sang DS cạnh tương ứng
'''

if __name__ == '__main__':
    n = int(input("nhap so luong dinh: "))
    a = [[0]*n for i in range(n)] #matrix ke cua dinh
    edge_list = []  # graph luu DS canh cua dinh

    #Input matrix ke
    for i in range(0,n):
        a[i] = [int(z) for z in input().split()]

    #Tao ra DS Canh
    for i in range(0,n):
        for j in range(0,n): #range i-> n đe tranh lap canh
            if a[i][j] == 1 and j>i:
                edge_list.append([i+1,j+1])
    print(edge_list)
    # #In ra DS Canh
    for i in range(len(edge_list)):
        print(*edge_list[i], end="\n")


'''
5
0 1 1 1 0
1 0 1 1 1
1 1 0 1 1
1 1 1 0 1
0 1 1 1 0

1 1 0 0 0 1
0 1 0 0 0 0
0 1 1 0 1 1
0 0 0 0 0 1
1 1 1 1 0 1
1 1 1 1 0 1

0 0 1 1 1 1
0 1 0 1 1 1
0 1 1 0 1 1
0 0 0 0 0 1
1 1 1 1 0 0
1 1 1 1 1 0

0 0 0 0 0 0 0 1
0 0 0 0 1 1 0 0
0 0 0 0 0 0 1 0
0 0 0 0 0 0 1 0
0 1 0 0 0 1 0 0
0 1 0 0 1 0 0 0
0 0 1 1 0 0 0 0
1 0 0 0 0 0 0 0
'''