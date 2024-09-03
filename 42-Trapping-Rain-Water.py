class Solution:
    def trap(self, height: List[int]) -> int:
        L, R = 0, len(height) - 1
        res = 0
        leftMax = height[L]
        rightMax = height[R]
        while L < R:
            if leftMax < rightMax:
                L += 1
                leftMax = max(leftMax, height[L])
                res += leftMax - height[L]
            else:
                R -= 1
                rightMax = max(rightMax, height[R])
                res += rightMax - height[R]
        return res
