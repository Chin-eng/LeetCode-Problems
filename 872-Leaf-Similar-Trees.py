# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        self.array1 = []
        self.array2 = []

        def store_leaves(root, array):
            
            if not root:
                return None

            left = store_leaves(root.left, array)
            right = store_leaves(root.right, array)

            if (not left) and (not right):
                array.append(root.val)
            
            return root
    

        store_leaves(root1, self.array1)
        store_leaves(root2, self.array2)

        return self.array1 == self.array2
