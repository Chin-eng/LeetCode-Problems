class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ans = []
        n = len(operations)
            
        for i in range(n):
            if operations[i] == 'C':
                ans.pop()
            elif operations[i] == '+':
                ans.append(ans[-1] + ans[-2])
            elif operations[i] == 'D':
                ans.append(2 * ans[-1])
            else:
                ans.append(int(operations[i]))
        return sum(ans)
            



        