from collections import deque
from collections import defaultdict

class Solution:
    def bfs(self,graph, visited, u):
        queue = deque()
        queue.append(u)
        visited[u] = True

        #Bước lạp
        while queue:
            v = queue.popleft() #lay dỉnh ở dau
            print(v, end=" ")
            for x in graph[v]:
                if visited[x] == False:
                    queue.append(x)
                    visited[x] = True
if __name__ == '__main__':
    n = int(input("nhap so luong dinh: "))
    m = int(input("nhap so luong canh: "))
    graph = defaultdict(list)  # graph luu DS ke cua dinh
    # Duyet m canh ->  nhap 2 dinh cua canh
    # Duyet m canh ->  nhap 2 đinh của canh
    for i in range(m):
        #input DS Canh
        x, y = [int(z) for z in input().split()]
        #Tao DS KE
        graph[x].append(y)
        graph[y].append(x)
    visited = [False] * (n+1)
    print(graph)
    print(Solution.bfs(Solution, graph, visited, 1))

'''
10 11
1 2
1 3
1 5
1 10
2 4
3 6
3 7
3 9
6 7
9 8
8 5
'''