# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:   
        
             
        def find_sum(node, current_sum):

            if not node:
                return False
 
            sumSoFar = current_sum + node.val

            if not node.left and not node.right and sumSoFar == targetSum:
                return True

            left = find_sum(node.left, sumSoFar)
            right = find_sum(node.right, sumSoFar)

            return left or right

        return find_sum(root, 0)