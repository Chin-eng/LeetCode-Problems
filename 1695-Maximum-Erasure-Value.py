class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        hashmap = defaultdict(int)

        left, ans = 0, 0
        for right in range(len(nums)):
            num_right = nums[right]
            while left <= right and num_right in hashmap:
                num_left = nums[left]
                hashmap[num_left] -= 1
                if hashmap[num_left] == 0:
                    hashmap.pop(num_left)
                left += 1 
            hashmap[num_right] += 1
            ans = max(ans, sum(nums[left:right+1]))

        return ans
        