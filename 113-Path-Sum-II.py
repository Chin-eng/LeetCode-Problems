# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.array = []
        
        def dfs(node, sumSoFar, arraylocal):

            if not node:
                return 

            arraylocal.append(node.val)
            currentSum = sumSoFar + node.val
            
            if currentSum == targetSum and (not node.left) and (not node.right):
                self.array.append(list(arraylocal))
            
            dfs(node.left, currentSum, arraylocal)
            dfs(node.right, currentSum, arraylocal)
            arraylocal.pop()
        
        dfs(root, 0, [])
        return self.array

