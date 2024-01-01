'''
Cho DS kề → chuyển sang DS Cạnh tương ứng
'''
from collections import defaultdict
if __name__ == '__main__':
    n = int(input("nhap so luong dinh: "))
    adj = defaultdict(list)  # graph luu DS ke cua dinh
    edge_list = []  # graph luu DS canh cua dinh

    #Input DS ke
    for i in range(n):
        adj[i].append([int(z) for z in input().split()])
        adj[i] = adj[i][0] #fix bug: loại bỏ dấu [] bị thừa
        # tạo adjacency_matrix
        for j in adj[i]:
            if j > i: #fix bug: bị lặp cạnh
                edge_list.append([i+1, j])

    # #In ra DS Canh
    for i in range(len(edge_list)):
        print(*edge_list[i], end="\n")


'''
5
2 3 4
1 3 4 5
1 2 4 5
1 2 3 5
2 3 4

6
1 1 2 6
1 2 2
3 3 5 6
6
3 6
1 3 4 5 6 6

3
1 1
2 2
3 3
'''