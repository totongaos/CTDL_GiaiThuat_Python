
'''
CHỊU THUA :((
'''
from collections import defaultdict
def graph_function(n,e,u,v):
    def dfs(u):
        print(graph[u])
        for v in graph[u]:
            if v not in seen:
                seen.append(v)
                dfs(v)
                parent[v] = u  # Ghi nhan cha của v là u
                print(seen,"-------------------")

    seen = []
    parent = [0] * (n + 1)
    graph = defaultdict(list)  # graph luu DS ke cua dinh

    # Duyet m canh ->  nhap 2 dinh cua canh
    for i in range(len(e)):
        x,y = [int(z) for z in e[i]]
        graph[x].append(y)
        graph[y].append(x)
    print(graph)
    seen.append(u)
    dfs(u)
    if (u not in seen) and (v not in seen): #check dỉnh t đã đc thăm với đỉnh s chưa
        return -1
    else: #Truy Vet dương di
        path = []
        while v!=u:
            path.append(v)
            v = parent[v]
        path.append(u)
        return len(path) -1
if __name__ == '__main__':
    n = 6
    e = [[1,3], [1,2], [2, 3], [3,4], [2,5], [4,6], [6,5], [4,5]]
    u = 1
    v = 5
    print(graph_function(n,e,u,v))