class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        seen = set()
       
        graph = defaultdict(list)
        n = len(isConnected)
        for i in range(n):
            for j in range(i+1, n):
                if isConnected[i][j]:
                    graph[i].append(j)
                    graph[j].append(i)
            
        def dfs(node):
            stack = [node]
            while stack:
                node = stack.pop()
                for neighbor in graph[node]:
                    if neighbor not in seen:
                        seen.add(neighbor)
                        stack.append(neighbor)
            
        
        ans = 0
        for node in range(n):
            if node not in seen:
                ans += 1
                seen.add(node)
                dfs(node)
        return ans
            
        
        
        

