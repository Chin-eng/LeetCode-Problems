# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:

        queue = deque([root])
        result = []
        while queue:
            length = len(queue)
            temp = [node.val for node in queue]
            result.append(temp)
            for _ in range(length):
                node = queue.popleft()                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        print(result)

        max_val = float('-inf')
        ans = 0
        for index, values in enumerate(result):
            if sum(values) > max_val:
                ans = index
                max_val = max(sum(values), max_val)
        return ans + 1

        