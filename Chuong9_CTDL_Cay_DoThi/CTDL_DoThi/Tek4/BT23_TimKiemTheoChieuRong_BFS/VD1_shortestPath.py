from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self,grid:list[list[int]]) -> int:
        if grid[0][0] == 1: return -1

        def valid(row, col):
            return 0 <= row < n and 0 <= col < n and grid[row][col] == 0

        n = len(grid)
        seen = {(0,0)}
        queue = deque([(0,0,1)]) #row, col, steps
        #directions 8 hướng: phải dưới trái trên ;
        # trái_trên trái_dưới phải_trên phải_dưới
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0),
                      (1, 1), (-1, -1), (1, -1), (-1, 1)]

        #Bước lạp
        while queue:
            row, col, steps = queue.popleft()
            if (row, col) == (n-1, n-1): return steps

            for dx, dy in directions:
                next_row, next_col = row + dy, col + dx
                if valid(next_row, next_col) and (next_row, next_col) not in seen:
                    seen.add((next_row, next_col))
                    queue.append((next_row,next_col,steps+1))

if __name__ == '__main__':
    n=6
    grid = [[0] * n for i in range(n)]  # matrix ke cua dinh

    # Input matrix ke
    for i in range(0, n):
        grid[i] = [int(z) for z in input().split()]
    print(grid)

    print(Solution.shortestPathBinaryMatrix(Solution,grid))
'''
0 0 1 1 1 1
0 1 0 1 1 1
0 1 1 0 1 1
0 0 0 0 0 1
1 1 1 1 0 0
1 1 1 1 1 0
'''