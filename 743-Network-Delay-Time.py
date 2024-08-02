class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {i:[] for i in range(n)}

        for source, target, weight in times:
            adj[source-1].append((target-1, weight))

        minHeap = [(0,k-1)]

        distances = [float('inf')] * n
        distances[k-1] = 0
        ans = 0
        while minHeap:
            weight, node = heapq.heappop(minHeap)

            if distances[node] < weight:
                continue

            for neighbor, neighborWeight in adj[node]:
                dist = weight + neighborWeight
                if distances[neighbor] > dist:
                    distances[neighbor] = dist
                    heapq.heappush(minHeap, (dist, neighbor))
        
        ans = max(distances)  
        return ans if ans != float('inf') else -1
            

        