'''
Giống VD1_SoLuongTinh của tek4_DFS
'''

from collections import defaultdict
from collections import deque
class Solution:
    def connectedComponent(self, adj):
        def bfs(u):
            queue = deque()
            queue.append(u)
            visted[u] = True
            while queue:
                node = queue.popleft()
                temp.append(node)
                for i in adj[node]:
                    if visted[i] == False:
                        queue.append(i)
                        visted[i] = True
            return temp



        n = len(adj)
        visted = [False] * (n + 1)
        ans = 0
        for i in range(1,n+1): #từ 1 đến <= n
            temp = []
            if visted[i] == False:
                ans += 1
                print(f"cac dinh of TPLT thu {ans}:", end=" ")

                print(bfs(i))
        if ans == 1:
            print("Do thi Lien Thong !!!")
            return ans
        else:
            print("Do KHONG thi Lien Thong !!!")
            return ans
#3. Ham main
if __name__ == '__main__':
    n = int(input("nhap so luong dinh: "))
    m = int(input("nhap so luong canh: "))
    graph = defaultdict(list)  # graph luu DS ke cua dinh
    # Duyet m canh ->  nhap 2 đinh của canh
    for i in range(m):
        # input Edge List
        x, y = [int(z) for z in input().split()]
        # Tao adjancency list
        graph[x].append(y)
        graph[y].append(x)
    print(graph, len(graph))
    #In số thành phần liên thông
    print("connected component: ",Solution.connectedComponent(Solution, graph))


'''
1 2
2 3
2 4
3 6
3 7
6 7
3 8
5 8
8 9
5 10
'''