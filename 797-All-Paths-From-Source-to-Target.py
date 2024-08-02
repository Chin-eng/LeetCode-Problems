class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        self.result = []

        def dfs(node, temp):
            temp.append(node)
            if node == len(graph) - 1:
                self.result.append(list(temp))
            for neighbor in graph[node]:
                dfs(neighbor, temp)
            temp.pop()
        dfs(0, [])
        return self.result

        