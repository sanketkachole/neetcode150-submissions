# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        # Stop if tree is empty
        if root is None:
            return 0

        # Create a queue containig the root
        queue = deque([root])
        counter = 0

        while queue:
            level_size = len(queue)
            
            for _ in range(level_size):
                node = queue.popleft()			
                
                # continue until queue become empty
                if node.left is not None:
                    queue.append(node.left)
                
                if node.right is not None:
                    queue.append(node.right)
                
            counter += 1

        return counter