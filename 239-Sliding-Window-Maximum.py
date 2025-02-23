class Solution(object):
    def maxSlidingWindow(self, nums, k):
        \\\
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        \\\

        if k == 0 or k == 1: return nums

        queue = deque([0])
        ans = []

        left = 0

        for right in range(len(nums)):
            prev = nums[queue[-1]]
            while queue and nums[right] >= prev:
                queue.pop()
                if queue:
                    prev = nums[queue[-1]]
            
            queue.append(right)

            while right - left + 1 == k:
                max_val = nums[queue[0]]
                ans.append(max_val)
                if left in queue:
                    queue.popleft()
                left += 1
                     
        return ans
        