'''
Cho DS cạnh → chuyển sang DS kề tương ứng
'''

from collections import defaultdict

if __name__ == '__main__':
    n = int(input("nhap so luong dinh: "))
    m = int(input("nhap so luong canh: "))
    graph = defaultdict(list) #graph luu DS ke cua dinh

    # Duyet m canh ->  nhap 2 đinh của canh
    for i in range(m):
        #input DS Canh
        x, y = [int(z) for z in input().split()]
        #Tao DS KE
        graph[x].append(y)
        graph[y].append(x)

    print(graph)
    # #In matran ke tuong ung adjacency_matrix
    for row in range(n):
        print(row,':',graph[row],end="\n")



'''
0 1
1 3
2 3
5 0
5 4
6 4
'''