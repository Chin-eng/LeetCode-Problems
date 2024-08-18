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

        def find_leaf_nodes(node, array):
            if not node:
                return None
            
            left = find_leaf_nodes(node.left, array)
            right = find_leaf_nodes(node.right, array)

            if not left and not right:
                array.append(node.val)
            
            return array
        print('tree 1')
        print(find_leaf_nodes(root1, self.array1))
        print('tree 2')
        print(find_leaf_nodes(root2, self.array2))

        tree1_leaf = find_leaf_nodes(root1, self.array1)
        tree2_leaf = find_leaf_nodes(root2, self.array2)
        return tree1_leaf == tree2_leaf

        