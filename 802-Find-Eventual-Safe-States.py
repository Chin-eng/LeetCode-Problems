class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        ans = []
        n = len(graph)
        
        safe = {}

        def dfs(node):

            if node in safe:
                return safe[node]

            safe[node] = False
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False

            safe[node] = True
            return True


        for node in range(n):
            if dfs(node):
                ans.append(node)
        return ans
            
        
        
        