# class TreeNode:
#     def __init__(self, val = 0, left=None, right=None)
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def isPalindrome(array):
            
            i = 0
            j = len(array) - 1
            while i < j:
                if (array[i] == None and array[j]) or (array[i] and array[j] == None):
                    return False
                if array[i] and array[j] and array[i].val != array[j].val:
                    return False
                i += 1
                j -= 1
            return True

        # queue = [2,2]
        # currentNode = 1

        queue = deque([root])

        while queue:
            queue_length = len(queue)
            for _ in range(queue_length):
                currentNode = queue.popleft()
                if currentNode:
                    queue.append(currentNode.left)
                    queue.append(currentNode.right)
                    
            if not isPalindrome(queue):
                return False
            
        return True

