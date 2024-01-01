'''
Giong bai 19 ở tek4
'''

from collections import defaultdict

def check(n, e, u, v):
    def dfs(node):
        # 4.2.1 xai for check peak con của peak vua duyet
        for peak in graph[node]:
            if peak not in seen:  # neu chua ở trong stack thì them vào
                seen.append(peak)
                dfs(peak)  # dequy den khi het dinh con

    graph = defaultdict(list)  # graph luu DS ke cua dinh
    seen = []
    # Chuyển Edge List -> Adjacency List
    for i in range(len(e)):
        x,y = [int(z) for z in e[i]]
        print(x,y)
        graph[x].append(y)
        graph[y].append(x)
    print(graph)

    # 4. Truy cap cac p.tu trong adjacency list
    if u not in seen:  # 4.1 check u và duyet các dinth của u
        seen.append(u)
        dfs(u)  # 4.2 duyet DFS
    print(seen)
    return u and v in seen

if __name__ == '__main__':
    n = 4
    e = [[1,2],[4,3]]
    u = 4
    v = 3
    print(check(n,e,u,v))