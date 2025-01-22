class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:

        def array_to_string(array):
            string = ''
            for num in array:
                string += "_" + str(num)
            return string

        grid_column = []

        for i in range(len(grid[0])):
            array = []
            for num in grid:
                array.append(num[i])
            grid_column.append(array)

        hashmap1 = defaultdict(int)
        hashmap2 = defaultdict(int)

        for num in grid:
            string_value = array_to_string(num)
            hashmap1[string_value] += 1
        
        for num in grid_column:
            string_value = array_to_string(num)
            hashmap2[string_value] += 1

        ans = 0
        
        for key in hashmap1:
            if key in hashmap2:
                value = hashmap1[key] * hashmap2[key]
                ans += value
        return ans 


        
        