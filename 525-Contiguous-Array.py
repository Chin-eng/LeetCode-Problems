class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        array = []
        for num in nums:
            if num == 0:
                array.append(-1)
            else:
                array.append(num)
        
        prefix = [array[0]]
        
        for i in range(1, len(array)):
            prefix.append(prefix[-1] + array[i])

        hashmap = defaultdict(int)
        hashmap[0] = -1

        ans = 0

        for i in range(len(prefix)):
            if prefix[i] in hashmap:
                ans = max(ans, i - hashmap[prefix[i]])
            if prefix[i] not in hashmap:
                hashmap[prefix[i]] = i 

        return ans

        