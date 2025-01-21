class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        hashmap = defaultdict(int)
        # print(cards.index(8))
        ans = float("inf")

        for index, card in enumerate(cards):
            if card in hashmap:
                ans = min(ans, index - hashmap[card] + 1)
            hashmap[card] = index
        
        return ans if ans != float("inf") else -1
        # return -1
                