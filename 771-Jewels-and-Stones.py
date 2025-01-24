class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels_hash = defaultdict(int)
        stones_hash = defaultdict(int)

        for jewel in jewels:
            jewels_hash[jewel] += 1
        
        for stone in stones:
            stones_hash[stone] += 1

        ans = 0

        for key in stones_hash:
            if key in jewels_hash:
                ans += stones_hash[key]

        return ans


        