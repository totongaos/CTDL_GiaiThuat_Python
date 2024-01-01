from collections import defaultdict

class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        #5.
        def dfs(node):
            stack = [node]
            print(stack,'----------------',node)
            while stack:
                node = stack.pop()
                for neighbor in graph[node]:
                    if neighbor not in seen:
                        seen.add(neighbor)
                        stack.append(neighbor)


        #1. build the graph
        n = len(isConnected)
        graph = defaultdict(list)
        #2. Duyet qua tưng node trong dothi
        for i in range(n):
            for j in range(i+1,n): #2.1 duyet cac node từ (i+1 -> n) tránh đg 2c
                if isConnected[i][j]: # isConnected[i][j] == 1 -> 2 node lân cận
                    #graph là unordered_map
                    graph[i].append(j)
                    graph[j].append(i)
        #3. khai bao bien kqua
        ans = 0
        seen = set()
        #4. Duyet qua tưng node trong dothi
        for i in range(n):
            if i not in seen:
                ans+=1
                seen.add(i)

                dfs(i) #4.duyet theo chieu sau

        return ans




#3. Ham main
if __name__ == '__main__':
    isConnected = [[0, 0, 0, 0, 0, 0, 0, 1],
                   [0, 0, 0, 0, 1, 1, 0, 0],
                   [0, 0, 0, 0, 0, 0, 1, 0],
                   [0, 0, 0, 0, 0, 0, 1, 0],
                   [0, 1, 0, 0, 0, 1, 0, 0],
                   [0, 1, 0, 0, 1, 0, 0, 0],
                   [0, 0, 1, 1, 0, 0, 0, 0],
                   [1, 0, 0, 0, 0, 0, 0, 0]]
    print(Solution.findCircleNum(Solution, isConnected))