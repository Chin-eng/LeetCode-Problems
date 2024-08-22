class Solution:
    def arrangeCoins(self, n: int) -> int:

        i = 0
        while i/2*(i+1) <= n:
            i += 1
        return i-1

        