class Solution:
    def isPathCrossing(self, path: str) -> bool:
        
        directions = set()

        directions.add((0,0))

        visited = (0, 0)

        for direction in path:
            if direction == "N":
                visited = (visited[0], visited[1] + 1)
                if visited in directions:
                    return True
            elif direction == "E":
                visited = (visited[0] + 1, visited[1])
                if visited in directions:
                    return True
            elif direction == "S":
                visited = (visited[0], visited[1] - 1)
                if visited in directions:
                    return True
            else:
                visited = (visited[0] - 1, visited[1])
                if visited in directions:
                    return True
           
            directions.add(visited)


        return False


        