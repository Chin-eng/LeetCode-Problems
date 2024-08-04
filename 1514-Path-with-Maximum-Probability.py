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
            currentSuccess, node = heapq.heappop(minHeap)
            if node == end_node:
                return -currentSuccess
            seen.add(node)
            for neighbor, neighborSucess in adj[node]:
                if neighbor not in seen:                  
                    heapq.heappush(minHeap, ((currentSuccess * neighborSucess), neighbor))
        return 0



        # for i in range(len(edges)):
        #     graph[edges[i][0]].append((edges[i][1], succProb[i]))
        #     graph[edges[i][1]].append((edges[i][0], succProb[i]))

        # seen = set()
        # minH = [[-1, start_node]]

        # while minH:
        #     prod, node = heapq.heappop(minH)
        #     if node == end_node:
        #         return -prod
        #     seen.add(node)
        #     for nei, neiCost in graph[node]:
        #         if nei not in seen:
        #             heapq.heappush(minH, [prod * neiCost, nei])

        # return 0






    

        