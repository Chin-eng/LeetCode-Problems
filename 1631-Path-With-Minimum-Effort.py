class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:

        rows, columns = len(heights), len(heights[0])

        minHeap = [(0, 0, 0)]
        seen = set()
        directions = [(0,1),(1,0), (0,-1), (-1,0)]

        def valid(row, col):
            return 0 <= row < rows and 0 <= col < columns and (row, col) not in seen

        while minHeap:
            diff, row, col = heapq.heappop(minHeap)
            if (row, col) in seen:
                continue
            
            seen.add((row, col))

            if (row, col) == (rows -1 , columns - 1):
                return diff

            for dx, dy in directions:
                next_row, next_col = row + dy, col + dx
                if not valid(next_row, next_col):
                    continue
                newDiff = max(diff, abs(heights[row][col] - heights[next_row][next_col]))
                heapq.heappush(minHeap, [newDiff, next_row, next_col])


        