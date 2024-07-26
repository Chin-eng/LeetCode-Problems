class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        rows, columns = len(board), len(board[0])

        directions = [(0,1), (1,0), (0,-1), (-1, 0)]
        seen = set()

        def onborder(row, col):
            return row == 0 or row == rows-1 or col == 0 or col == columns-1
        
        def inRange(row, col):
            return 0 <= row < rows and 0<= col < columns

        def capture(row, col):
            seen.add((row, col))
            for dx, dy in directions:
                next_row, next_col = row + dy, col + dx
                if inRange(next_row, next_col) and (next_row, next_col) not in seen and board[next_row][next_col] == "O":
                    capture(next_row, next_col)

        for row in range(rows):
            for col in range(columns):
                if board[row][col] == "O" and onborder(row, col):
                    capture(row, col)

        for row in range(rows):
            for col in range(columns):
                if board[row][col] == "O" and (row, col) not in seen:
                    board[row][col] = "X"
