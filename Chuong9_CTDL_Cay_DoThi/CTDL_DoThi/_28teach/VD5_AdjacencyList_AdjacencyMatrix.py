'''
Cho DS kề → chuyển sang ma trận kề tương ứng
'''
from collections import defaultdict
if __name__ == '__main__':
    n = int(input("nhap so luong dinh: "))
    a = [[0]*n for i in range(n)] #matrix ke cua dinh
    adj = defaultdict(list)  # graph luu DS ke cua dinh

    #Input DS ke
    for i in range(n):
        adj[i].append([int(z) for z in input().split()])
        adj[i] = adj[i][0] #loại bỏ dấu [] bị thừa
        # tạo adjacency_matrix
        for j in adj[i]:
            a[i][j-1] = 1
    # print(adj)

    #In matran ke tuong ung adjacency_matrix
    for row in range(n):
        for col in range(n):
            print(a[row][col],end=" ")
        print("", end="\n")


'''
5
2 3 4
1 3 4 5
1 2 4 5
1 2 3 5
2 3 4
'''