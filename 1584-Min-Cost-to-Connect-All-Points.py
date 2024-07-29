class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        N = len(points)

        adj = {i:[] for i in range(N)}

        for i in range(N):
            x1, y1 = points[i]
            for j in range(i+1, N):
                x2, y2 = points[j]
                distance = abs(x1-x2) + abs(y1-y2)
                adj[i].append([distance, j])
                adj[j].append([distance, i])
        
        seen = set()
        result = 0
        minHeap = [[0,0]]
        while len(seen) < N:
            cost, node = heapq.heappop(minHeap)
            if node in seen:
                continue
            result += cost
            seen.add(node)
            for neighborCost, neighbor in adj[node]:
                if neighbor not in seen:
                    heapq.heappush(minHeap, [neighborCost, neighbor])
        return result
        