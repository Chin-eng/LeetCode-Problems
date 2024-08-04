class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = {i: [] for i in range(n)}

        for source, target, cost in flights:
            adj[source].append((target, cost))

        # (cost, current_node, stops)
        minHeap = [(0, src, 0)]
        costs = {(src, 0): 0}

        while minHeap:
            weight, node, stops = heapq.heappop(minHeap)
            if node == dst:
                return weight

            if stops > k:
                continue

            for neighbor, neighborCost in adj[node]:
                newCost = weight + neighborCost
                if stops + 1 <= k + 1 and (neighbor, stops + 1) not in costs or newCost < costs.get((neighbor, stops + 1), float('inf')):
                    costs[(neighbor, stops + 1)] = newCost
                    heapq.heappush(minHeap, (newCost, neighbor, stops + 1))

        return -1
