# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        def dfs(node, maxSoFar):
            if node:
                maxSoFar = max(maxSoFar, node.val)
                if node.val >= maxSoFar:
                    self.count += 1           
                dfs(node.left, maxSoFar)
                dfs(node.right, maxSoFar)
        dfs(root, root.val)   
        return self.count


        # self.count = 0
        # def dfs(node, maxSoFar):
        #     if node:
        #         maxSoFar = max(maxSoFar, node.val)
        #         if node.val >= maxSoFar:
        #             self.count += 1
        #         dfs(node.left, maxSoFar)
        #         dfs(node.right, maxSoFar)
        # dfs(root, root.val)
        # return self.count
            
            
        