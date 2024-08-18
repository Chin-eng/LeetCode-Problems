# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:

        self.depth = 0
        
        def dfs(node, direction, depth):
            if node:
                self.depth = max(self.depth, depth)
             
                if direction == 'right':
                    dfs(node.right, 'left', depth + 1)
                    dfs(node.right, 'right', 0)
                
                if direction == "left":
                    dfs(node.left, 'right', depth + 1)
                    dfs(node.left, 'left', 0)

        dfs(root, 'right', 0)
        dfs(root, 'left', 0)
        
        return self.depth 


        