class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {i:[] for i in range(1, n+1)}

        for source, target, weight in times:
            adj[source].append((target, weight))
        
        seen = set()
        minHeap = [(0,k)]
        ans = 0
        while minHeap:
            weight, node = heapq.heappop(minHeap)
            if node in seen:
                continue
            seen.add(node)
            ans = max(weight, ans)
            for neighbor, neighborWeight in adj[node]:
                if neighbor not in seen:
                    heapq.heappush(minHeap, (neighborWeight + weight, neighbor)) 
        return ans if len(seen) == n else -1

        