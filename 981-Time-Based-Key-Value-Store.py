class TimeMap:

    def __init__(self):
        self.dictionary = {}  

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dictionary:
            self.dictionary[key] = []

        self.dictionary[key].append([value, timestamp]) 

        # obj.set('foo', 'bar1', 1)
        # obj.set('foo', 'bar2', 2)
        # obj.set('foo', 'bar3', 10000)

        # {foo: [[bar1, 1], [bar2, 2], [bar3, 10000]]}

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dictionary:
            return ''
        left, right = 0, len(self.dictionary[key]) - 1
        array = self.dictionary[key]

        while left <= right:
            mid = (left + right) // 2

            if timestamp == array[mid][1]:
                return array[mid][0]
            elif timestamp > array[mid][1]:
                left = mid + 1
            else:
                right = mid - 1
        
        return array[right][0] if right >= 0 else ''
            
            




# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)