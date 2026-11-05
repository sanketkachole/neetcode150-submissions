# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        # If the tree is empty, return []
        if root is None:
            return []
        # Initialize an empty main result list
        main_list = []
        # Create a queue containing the root node
        queue = deque([root])
        # Continue while the queue is not empty:
        while queue:
            # Create a new empty list for the current level
            level_list = []
            # Record level_size = number of nodes currently in the queue
            level_size = len(queue)
            # Repeat exactly level_size times:
            for _ in range(level_size):
                # Remove the first node from the queue
                node = queue.popleft()
                # Append the node's value to the current-level list
                level_list.append(node.val)
                # If the node has a left child:
                    # Add the left child to the queue
                if node.left is not None:
                    queue.append(node.left)
                # If the node has a right child:
                    # Add the right child to the queue
                if node.right is not None:
                    queue.append(node.right)
            # Append the completed current-level list to the main result list
            main_list.append(level_list)
        # Return the main result list
        return main_list

