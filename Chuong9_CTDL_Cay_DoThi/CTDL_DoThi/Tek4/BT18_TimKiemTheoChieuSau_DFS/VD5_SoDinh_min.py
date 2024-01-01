'''Ví dụ 5: Số đỉnh tối thiểu để nối tới tất cả các đỉnh
Cho một đồ thị không chu trình có hướng,
với n đỉnh được đánh số từ 0 đến n-1 và mảng edges trong đó edges[i] = [x, y] là một cạnh có hướng từ đỉnh x đến đỉnh y.

Tìm tập hợp các đỉnh nhỏ nhất mà từ đó tất cả các đỉnh trong đồ thị đều có thể nối tới. (dinh bac in = 0)
'''

class Solution:
    def findSmallestSetOfVertices(self,n,edge_list: list[list[int]]) -> int:
        seen = [0]*n
        for _,i in edge_list:
            seen[i] +=1
        return [x for x in range(n) if seen[x]==0]

#3. Ham main
if __name__ == '__main__':
    edge_list = [[0, 2],
                 [1, 2],
                 [5, 4],
                 [2, 4],
                 [2, 7],
                 [6, 3],
                 [6, 7]]
    n = 8 #dỉnh của grid

    print(Solution.findSmallestSetOfVertices(Solution,n, edge_list))
