class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        edges = [0] * n
        seen = set()
        for src, dst in roads:
            edges[src] += 1
            edges[dst] += 1
            seen.add((min(src, dst), max(src, dst)))
        
        max_rank = 0
        for i in range(n):
            for j in range(i+1, n):
                current_rank = edges[i] + edges[j]
                if (i, j) in seen:
                    current_rank -=1
                max_rank = max(current_rank, max_rank)
        return max_rank



        