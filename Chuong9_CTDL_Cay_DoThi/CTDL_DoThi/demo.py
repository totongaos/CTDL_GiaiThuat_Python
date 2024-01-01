from collections import defaultdict

M=0
def graphFunction(n, a, u, v):
    if u == v : return -1
    def dfs(node, count):
        global M
        # print(node,'node+++++++++++++')
        # 4.2.1 xai for check peak con cua peak vua duyet
        for i in graph[node]:

            if i not in seen :  # neu chua o trong stack thi them vao
                seen.append(i)
                M = max(M, count + 1)
                if i == v: break
                else:

                    dfs(i, count+1)  # dequy den khi het dinh con

    global M
    graph = defaultdict(list)  # graph luu DS ke cua dinh
    seen = [u]
    # Duyet m canh ->  nhap 2 dinh cua canh
    for i in range(len(a)):
        x,y = [int(z) for z in a[i]]
        graph[x].append(y)
        graph[y].append(x)

    # print(graph)
    ans= 0
    for peak in range(u,n):
        ans += 1
        if ans > 1:
            if u not in seen or v not in seen:
                return -1
        #     if i == v: break
        elif ans==1:
            seen.append(peak)
            dfs(peak,1)
            # print(len(seen))

    print(seen, len(seen))
    # print(M,'///////////////')
    # if M > 1:
    return (M) -1
    # else:
    #     return (-1)

if __name__ == '__main__':
    n = 6
    a = [[1,3], [1,2], [2, 3], [3,4], [2,5], [4,6], [6,5], [4,5]]
    u = 1
    v = 5
    print(graphFunction(n,a,u,v))