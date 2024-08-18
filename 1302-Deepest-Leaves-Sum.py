# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:

        if not root:
            return None
        
        queue = deque([root])
        
        while queue:
            local_array = []
            current_len = len(queue)
            for _ in range(current_len):
                node = queue.popleft()
                local_array.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return sum(local_array)


        