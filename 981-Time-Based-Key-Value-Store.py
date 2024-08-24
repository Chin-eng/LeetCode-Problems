class TimeMap:

    def __init__(self):
        self.dictionary = {}  

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dictionary:
            self.dictionary[key] = []

        self.dictionary[key].append([value, timestamp]) 

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




        # { love: [ ['high', 10], ['low', 20] ] }

        
        # obj.get('love', 5)




        # obj.set('foo', 'bar', 1)
        # obj.set('foo', 'bar', 3)
        # obj.set('foo', 'bar', 2)

        # { foo: [ ['bar' 1], ['bar', 2], ['bar', 3] ] }

        # obj.get('bar', 7)

        # [ ['bar' 1], ['bar', 3], ['bar', 2] ]


            
            




# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)