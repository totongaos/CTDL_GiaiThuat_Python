from collections import defaultdict


def graphFunction(n, a, u, v):
    def dfs(node):
        # 4.2.1 xai for check peak con cua peak vua duyet
        for peak in graph[node]:
            if peak not in seen:  # neu chua o trong stack thi them vao
                seen.append(peak)
                dfs(peak)  # dequy den khi het dinh con


    graph = defaultdict(list)  # graph luu DS ke cua dinh
    seen = []
    # Duyet m canh ->  nhap 2 dinh cua canh
    for i in range(len(a)):
        x,y = [int(z) for z in a[i]]
        graph[x].append(y)
        graph[y].append(x)
    print(graph)
    seen.append(u)
    for i in range(u,n):
        for peak in graph[i]:
            if peak not in seen:
                print(peak)
                seen.append(peak)
                dfs(peak)  # 4.2 duyet DFS
    print(seen)
    if (u in seen) and (v in seen):
        return (len(seen)-1)
    else:
        return -1

if __name__ == '__main__':
    n = 6
    a = [[1,3], [1,2], [2, 3], [3,4], [2,5], [4,6], [6,5], [4,5]]
    u = 1
    v = 5
    print(graphFunction(n,a,u,v))
'''
[[1,3], [4,2], [2, 3], [3,4], [2,5], [4,6], [6,5], [4,5]]
'''