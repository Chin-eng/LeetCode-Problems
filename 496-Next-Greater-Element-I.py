class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        n = len(nums2)
        great_map = {n: index for index, n in enumerate(nums1)}
        result = [-1] * len(nums1)
        
        for i in range(n):
            if nums2[i] in great_map:
                for j in range(i + 1, n):
                    if nums2[i] < nums2[j]:
                        index = great_map[nums2[i]]
                        result[index] = nums2[j]
                        break
        return result




        


        