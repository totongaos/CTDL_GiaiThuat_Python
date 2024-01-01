'''
Giống VD1_SoLuongTinh của tek4_DFS
'''

from collections import defaultdict
from collections import deque
class Solution:
    def connectedComponent(self, adj):
        def dfs(u):
            temp.append(u) #luu cac TPLT của u
            # print(u, end=" ")
            for i in adj[u]:
                if i not in seen:
                    seen.append(i)
                    dfs(i)
            return temp


        seen = []
        n = len(adj)
        ans = 0
        for i in range(1,n+1): #từ 1 đến <= n
            temp = []
            if i not in seen:
                ans += 1
                seen.append(i)
                print(f"cac dinh of TPLT thu {ans}:", end=" ")

                print(dfs(i))

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