'''Ví dụ 3:
Sắp xếp lại các tuyến đường để tất cả các con đường đều dẫn đến thành phố Zero
Có n thành phố được đánh số từ 0 đến n - 1 và n - 1 con đường sao cho chỉ có một con đường duy nhất để di chuyển giữa hai thành phố.
Các con đường được biểu thị bằng connections trong đó connections[i] = [x, y] là con đường từ thành phố x đến thành phố y.
Các cạnh là có hướng.
Bạn cần hoán đổi hướng của các cạnh để mọi thành phố đều hướng đến thành phố 0.
Trả về số lần hoán đổi tối thiểu cần thực hiện.
'''

from collections import defaultdict
class Solution:
    def minReorder(self, n ,edge_list: list[list[int]]) -> int:
        # 3. Ham dfs
        def dfs(node):
            ans = 0
            for i in graph[node]: #truy cap các dg của dinh
                if i not in seen:
                    if (node, i) not in road: #check có doan dg nao ngc ko?
                        ans+=1
                    # print(node, i, ans)
                    seen.append(i)
                    ans += dfs(i)
            # print(seen)
            return ans

        road = set() #luu tuyen dg ban đàu
        graph = defaultdict(list)  # graph luu DS ke cua dinh
        for x, y in edge_list:
            graph[x].append(y)
            graph[y].append(x)
            road.add((x,y)) #luu tuyen dg ban đàu
        # print(graph,'\n', road)

        seen = [0] #theo doi cac nut dã truy cap
        return dfs(0)



#3. Ham main
if __name__ == '__main__':
    edge_list = [[0, 1],
                 [1, 3],
                 [2, 3],
                 [5, 0],
                 [5, 4],
                 [6, 4]]

    n = 7 #dỉnh của grid

    print(Solution.minReorder(Solution,n, edge_list))

'''
0 : [1, 5]
1 : [0, 3]
2 : [3]
3 : [1, 2]
4 : [5, 6]
5 : [0, 4]
6 : [4]
[[0, 1],
[1, 3],
[2, 3],
[5, 0],
[5, 4],
[6, 4]]
'''