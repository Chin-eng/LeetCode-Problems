# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def depth(node):
            if not node:
                return 0
            
            left = depth(node.left)
            right = depth(node.right)

            if left == 0 and right == 0:
                return 1
            
            return max(left, right) + 1
        
        def balanced(node):
            if not node:
                return True

            left = balanced(node.left)
            right = balanced(node.right)

            leftDepth = depth(node.left)
            rightDepth = depth(node.right)

            if abs(leftDepth - rightDepth) > 1:
                return False
            
            return left and right
        
        return balanced(root)
