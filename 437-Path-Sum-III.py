# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        cache = {0 : 1}
        self.result = 0

        def dfs(node, currentPathSum, cache):

            if not node:
                return

            currentPathSum += node.val
            oldPathSum = currentPathSum - targetSum
            self.result += cache.get(oldPathSum, 0)

            cache[currentPathSum] = cache.get(currentPathSum, 0) + 1

            dfs(node.left, currentPathSum, cache)
            dfs(node.right, currentPathSum, cache)

            cache[currentPathSum] -= 1
        
        dfs(root, 0, cache)
        return self.result 


