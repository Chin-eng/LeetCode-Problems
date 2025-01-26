class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        startSet = set()
        endSet = set()

        for start, end in paths:
            startSet.add(start)
            endSet.add(end)

        for city in startSet:
            if city in endSet:
                endSet.remove(city)

        return str(list(endSet)[0])
        
        