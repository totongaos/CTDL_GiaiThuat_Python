'''Tìm đường đi giữa 2 đỉnh trên đồ thị:
(có hướng && vô hướng) code tương tự thuật toán dfs & bfs
nhưng duy trì thêm mảng parent để truy vết đường đi.
Giả sử cần truy vết đường đi từ đỉnh s -> t. Ta gọi bfs(s) || dfs(s)

Đỉnh   | 1 | 2 | 3 | 6 | 7 |      | 5 | 8 | 9 |      | 10 |
Parent | 0 | 1 | 2 | 3 | 6 |


Từ bài 1 ở codelearn && bai 19 ở tek4 -> truy vet dương di từ s->t
'''

from collections import defaultdict
class Solution:
    def path(self, adj, s, t, n):
        def dfs(u):
            seen[u] = True
            temp.append(u) #luu cac TPLT của u
            # print(u, end=" ")
            for v in adj[u]:
                if seen[v] == False:
                    seen[v] = True
                    dfs(v)
                    parent[v] = u #Ghi nhan cha của v là u
            return temp

        seen = [False]*(n+1)
        parent = [0]*(n+1)
        temp = []

        dfs(s)
        if seen[t] == False: #check dỉnh t đã đc thăm với đỉnh s chưa
            return "Khong co dương dan tơi dinh t"
        else: #Truy Vet dương di
            path = []
            while t!=s:
                path.append(t)
                t = parent[t]
            path.append(s)
            path.reverse()
            return path

#3. Ham main
if __name__ == '__main__':
    n = int(input("nhap so luong dinh: "))
    m = int(input("nhap so luong canh: "))
    s = int(input("nhap dinh s: "))
    t = int(input("nhap dinh t: "))
    graph = defaultdict(list)  # graph luu DS ke cua dinh
    # # Chuyển Edge List -> Adjacency List
    for i in range(m):
        # input Edge List
        x, y = [int(z) for z in input().split()]
        # Tao adjancency list
        graph[x].append(y)
        graph[y].append(x)
    print(graph, len(graph))
    #In số thành phần liên thông
    print("connected component: ",Solution.path(Solution, graph, s, t, n))


'''
1 2
2 3
2 4
3 6
3 7
6 7
5 8
8 9    10-8
[[1, 2], [2, 3] , [2, 4], [3, 6], [3, 7]]
'''