# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        queue = deque([root])
        result = []

        

        # queue = [9, 20]
        # temp = [9]
        # average = [3] / 1
        # result = [3]

        while queue:
            length = len(queue)
            temp = []
            for _ in range(length):
                node = queue.popleft()
                temp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            average = sum(temp) / len(temp)
            result.append(average)
        
        return result