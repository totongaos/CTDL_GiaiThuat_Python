from collections import deque
from collections import defaultdict
def graph_function(n,e,u,v):
    def bfs(u):
        queue = deque()
        queue.append(u)
        seen[u] = True
        while queue:
            node = queue.popleft()
            for v in graph[node]:
                if seen[v] == False:
                    queue.append(v)
                    seen[v] = True
                    parent[v] = node  # Ghi nhan cha của v là u

    seen = [False]*(n+1)
    parent = [0]*(n+1)
    graph = defaultdict(list)  # graph luu DS ke cua dinh

    # Duyet m canh ->  nhap 2 dinh cua canh
    for i in range(len(e)):
        x,y = [int(z) for z in e[i]]
        graph[x].append(y)
        graph[y].append(x)
    bfs(u)
    if seen[v] == False: #check dỉnh t đã đc thăm với đỉnh s chưa
        return -1
    else: #Truy Vet dương di
        path = []
        while v!=u:
            path.append(v)
            v = parent[v]
        path.append(u)
        path.reverse()
        return len(path) -1
if __name__ == '__main__':
    n = 4
    e = [[1,2],[3,4]]
    u = 1
    v = 2
    print(graph_function(n,e,u,v))