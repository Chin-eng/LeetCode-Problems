class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        n = len(nums2)
        great_map = {n: index for index, n in enumerate(nums1)}
        result = [-1] * len(nums1)


        stack = []

        for i in range(len(nums2)):
            curr = nums2[i]
            while stack and curr > stack[-1]:
                val = stack.pop()
                index = great_map[val]
                result[index] = curr
            if curr in great_map:
                stack.append(curr)
        return result




        


        