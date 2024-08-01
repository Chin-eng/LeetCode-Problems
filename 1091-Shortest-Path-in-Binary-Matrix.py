class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        rows, columns = len(grid), len(grid[0])
        
        
        if grid[0][0] != 0 or grid[rows-1][columns-1] != 0:
            return -1

        queue = deque([(0,0, 1)])

        directions = [(0,1), (1,0), (-1,0), (0,-1), (1,1), (1,-1), (-1,-1), (-1, 1)]
        seen = {(0,0)}

        def valid(row, col):
            return 0<= row < rows and 0<= col < columns and grid[row][col] == 0
        
        while queue:
            row, col, steps = queue.popleft()
            if (row, col) == (rows-1, columns-1):
                return steps
            for dx, dy in directions:
                next_row, next_col = row + dy, col + dx
                if valid(next_row, next_col) and (next_row, next_col) not in seen:
                    seen.add((next_row, next_col)) 
                    queue.append((next_row, next_col, steps + 1))
        return -1