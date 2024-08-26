class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        starts = []
        stops = []

        for starting, ending in flowers:
            starts.append(starting)
            stops.append(ending + 1)

        sorted_start = sorted(starts)
        sorted_stops = sorted(stops)

        ans = []

        for person in people:
            i = bisect_right(sorted_start, person)
            j = bisect_right(sorted_stops, person)
            ans.append(i-j)

        return ans



        
        
        
        