class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = {i: [] for i in range(n)}

        for i in range(len(edges)):
            source, target = edges[i]
            currentSucess = succProb[i]
            adj[source].append((target, currentSucess))
            adj[target].append((source, currentSucess))

        seen = set()
        minHeap = [(-1, start_node)]

        while minHeap:
            prob, node = heapq.heappop(minHeap)
            if node == end_node:
                return - prob
            if node in seen:
                continue
            seen.add(node)
            for neighbor, neighborProb in adj[node]:
                if neighbor not in seen:
                    heapq.heappush(minHeap, (neighborProb * prob, neighbor))
        return 0





    

        