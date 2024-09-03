class Solution:
    def trap(self, height: List[int]) -> int:
        minLeft = [0] * len(height)
        minRight = [0] * len(height)
        current_max_left = 0
        for i in range(len(height)):
            minLeft[i] = current_max_left
            current_max_left = max(height[i], current_max_left)

        current_max_right = 0
        for i in range(len(height)-1, -1, -1):
            minRight[i] = max(current_max_right, minRight[i])
            current_max_right = max(height[i], current_max_right)
        
        ans = [0] * len(height)

        for i in range(len(height)):
            ans[i] = min(minLeft[i], minRight[i]) - height[i]

        print(ans)
        
        res = 0
        for i in range(len(height)):
            if ans[i] > 0:
                res += ans[i]

        return res

        