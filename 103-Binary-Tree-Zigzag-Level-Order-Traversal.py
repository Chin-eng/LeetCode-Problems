# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
    
        queue = deque([root])
        ans = []
        count = 0
        while queue:
            current_length = len(queue)
            current_row = []
            count += 1
            for _ in range(current_length):
                node = queue.popleft()
                current_row.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if count % 2 == 1:
                ans.append(current_row)
            else:
                ans.append(current_row[::-1])
        return ans
            
        