'''
Số lượng đảo
Cho grid nhị phân 2D có kích thước m x n biểu thị bản đồ 1 (đất liền) và 0 (nước), trả về số lượng đảo.
Hòn đảo được bao quanh bởi nước và được hình thành bằng cách kết nối các vùng đất liền kề theo chiều ngang hoặc chiều dọc.
'''


class Solution:
    def numIslands(self, grid: list[list[int]]) -> int:
        #4. Ham valid -> check ô có hợp lệ thăm ko?
        def valid(row, col):
            return (0 <= row < m) and (0 <= col < n) and (grid[row][col] ==1)

        #3. Ham dfs
        def dfs(row,col):
            for dx, dy in directions:
                next_row, next_col = row + dy, col + dx
                if valid(next_row, next_col) and (next_row,next_col) not in seen:
                    seen.add((next_row, next_col))
                    dfs(next_row, next_col)

        #1. khai báo directions lưu hướng đi có thể của thuật toán
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        seen = set()
        #1. khai bao kich thuoc cua grid 2c
        m = len(grid)
        n = len(grid[0])
        ans = 0

        #2. Duyet qua tưng node trong dothi
        for row in range(m):
            for col in range(n): #2.1 duyet cac node từ (i+1 -> n) tránh đg 2c
                if (grid[row][col] == 1) and ((row,col) not in seen):
                    ans+=1
                    seen.add((row,col))
                    dfs(row,col)

        return ans

#3. Ham main
if __name__ == '__main__':
    grid = [[1,1,0,0,0,1],
            [0,1,0,0,0,0],
            [0,1,1,0,1,1],
            [0,0,0,0,0,1],
            [1,1,1,1,0,1],
            [1,1,1,1,0,1]]

    print(Solution.numIslands(Solution, grid))

'''
[[1,1,0,0,0,1],
[0,1,0,0,0,0],
[0,1,1,0,1,1],
[0,0,0,0,0,1],
[1,1,1,1,0,1],
[1,1,1,1,0,1]]

[[1,0,0],
[0,1,0],
[1,0,1]]
'''