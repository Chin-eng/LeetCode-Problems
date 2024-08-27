class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        result = []
        nums = sorted(nums)
        for number in queries:
            current_sum = 0
            count = 0
            index = 0
            while index < len(nums):
                current_sum += nums[index]
                if number >= current_sum:
                    count += 1
                else:
                    current_sum -= nums[index]
                index += 1
            result.append(count)
        return result


        
        
        