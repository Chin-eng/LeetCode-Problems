class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:

        winnerHash = defaultdict(int)
        loserHash = defaultdict(int)

        notLost = []
        oneLoss = []

        for winner, loser in matches:
            winnerHash[winner] += 1
            loserHash[loser] += 1
        
        for key in winnerHash:
            if key not in loserHash:
                notLost.append(key)
        
        for key in loserHash:
            if loserHash[key] == 1:
                oneLoss.append(key)

        return [sorted(notLost), sorted(oneLoss)]
        