'''
Cho Adjacency Matrix chuyển đổi sang Adjacency List và duyet DFS
'''

from collections import defaultdict

class Solution:
	#5.
    def display(self, isConnected: list[list[int]]) -> int:
        #4.2 Ham duy DFS
        def dfs(node):
            # 4.2.1 xai for check peak con của peak vua duyet
            for peak in adj[node]:
                if peak not in stack: #neu chua ở trong stack thì them vào
                    stack.append(peak)
                    dfs(peak) #dequy den khi het dinh con

        #1. build the adjacency list
        n = len(isConnected)
        adj = defaultdict(list)
        #2. tao stack chua cac dinh sẽ dc duyet
        stack = []
        #3. Tao ra DS ke
        for i in range(n):
            for j in range(n):  # range i-> n đe tranh lap canh

                if isConnected[i][j]==1 and j>i:
                    adj[i].append(j)
                    adj[j].append(i)
        print(adj)
        #4. Truy cap cac p.tu trong adjacency list
        for peak in range(1,n):
            if peak not in stack: #4.1 check peak đã đc duyet chưa? nếu chưa thì them vao
                stack.append(peak)
                dfs(peak) #4.2 duyet DFS
            # print(row,':',adj[row],end="\n") #In adjacency list
        print('Peak list approved by DFS in_order: ', end=" ")
        #5. return stack các peak đã đc duyet
        return stack
#3. Ham main
if __name__ == '__main__':
    isConnected = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
                   [0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
                   [0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
                   [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                   [0, 1, 0, 0, 0, 0, 0, 1, 1, 1],
                   [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
                   [0, 0, 0, 0, 0, 1, 0, 0, 1, 0]]
    print(Solution.display(Solution, isConnected))

'''
1 2
1 3
1 5
2 4
5 8
3 6
5 7
5 9
8 9

1 : [2, 3, 5]
2 : [1, 4]
3 : [1, 6]
4 : [2]
5 : [1, 8, 7, 9]
6 : [3]
7 : [5]
8 : [5, 9]
'''