class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        incoming = defaultdict(int)
        outgoing = defaultdict(int)

        for src, dst in trust:
            incoming[src] += 1
            outgoing[dst] += 1
        
        for i in range(1, n + 1):
            if outgoing[i] == n - 1 and incoming[i] == 0:
                return i
        return -1 
        




        
        


        