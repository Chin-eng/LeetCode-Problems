class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:

        # nums = [7, 4, 3, 9, 1, 8, 5, 2, 6]  k = 3

        # prefix = [0, 7, 11, 14, 23, 24, 32, 37, 39, 45]
        


        n = len(nums)

        res = [-1] * n
        
        prefix = [0]
        for i in range(n):
            prefix.append(prefix[-1] + nums[i])

        window_size = 2 * k + 1

        for i in range(k, n-k):
            left, right = i-k, i+k
            sumSoFar = prefix[right+1] - prefix[left]
            average = sumSoFar // window_size
            res[i] = average
        
        return res
