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
            while i <= j:
                if array[i] != array[j]:
                    return False
                i += 1
                j -= 1
            return True

        queue = deque([root])

        # queue = [2,2]
        # queue_length = 1
        # localArray = [\null\, 3, 2]

        while queue:
            localArray = []
            queue_length = len(queue)
            for _ in range(queue_length):
                currentNode = queue.popleft()
                if currentNode.left:
                    localArray.append(currentNode.left.val)
                    queue.append(currentNode.left)
                else:
                    localArray.append(\null\)
                if currentNode.right:
                    localArray.append(currentNode.right.val)
                    queue.append(currentNode.right)
                else:
                    localArray.append(\null\)

            if not isPalindrome(localArray):
                return False
            
        return True

