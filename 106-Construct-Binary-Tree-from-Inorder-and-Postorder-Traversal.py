# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        def dfs(inorder, postorder):

            if not postorder and not inorder:
                return None
            
            print(postorder[-1])
            node = TreeNode(postorder[-1])

            mid = inorder.index(postorder[-1])

            node.right = dfs(inorder[mid+1:], postorder[mid:-1])
            node.left = dfs(inorder[:mid], postorder[:mid])

            return node
        
        return dfs(inorder, postorder)
            
        