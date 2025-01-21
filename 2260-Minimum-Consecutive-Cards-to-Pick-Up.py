class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        hashmap = defaultdict(list)
        for i in range(len(cards)):
            hashmap[cards[i]].append(i)

        hashmap_values = hashmap.values()
        
        ans = float("inf")

        for value in hashmap_values:
            array = value
            for i in range(1, len(array)):
                ans = min(ans, array[i] - array[i-1] + 1)

        return ans if ans != float("inf") else -1

        