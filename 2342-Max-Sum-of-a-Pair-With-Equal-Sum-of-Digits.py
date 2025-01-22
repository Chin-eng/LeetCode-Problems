class Solution:
    def maximumSum(self, nums: List[int]) -> int:

        hashmap = defaultdict(list)

        def get_digit_sum(num):
            sum_value = 0
            while num:
                sum_value += num % 10
                num //= 10
            return sum_value

        for num in nums:
            
            digit_sum = get_digit_sum(num)
            
            if digit_sum not in hashmap:
                hashmap[digit_sum] = (num, -1)
            else:
                largest, second_largest = hashmap[digit_sum]
                if num > largest:
                    second_largest = largest
                    largest = num
                elif num > second_largest:
                    second_largest = num  
                
                hashmap[digit_sum] = (largest, second_largest)       
        
        print(hashmap.values())

        ans = float("-inf")

        for value in hashmap.values():
            if value[1] != -1:
                ans = max(ans, sum(value))

        return ans if ans != float("-inf") else -1