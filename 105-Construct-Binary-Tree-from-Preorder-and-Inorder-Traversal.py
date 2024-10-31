# Definition for a binary tree node.
# class TreeNode:

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        def dfs(preorder, inorder):

            if not preorder or not inorder:
                return None

            node = TreeNode(preorder[0]) 
            
            mid = inorder.index(preorder[0]) 

            node.left = dfs(preorder[1:mid + 1], inorder[:mid])

            node.right = dfs(preorder[mid + 1:], inorder[mid + 1:])

            return node
        
        return dfs(preorder, inorder)

