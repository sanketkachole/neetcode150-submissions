# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
		# Step 1: Base case
		# If root is None, return None
        if root is None:
            return
	
        # Step 2: Swap the children of the current node
        # Store root.left in a temporary variable
        # Assign root.right to root.left
        # Assign temporary to root.right
        temporary = root.left
        root.left = root.right
        root.right = temporary

        # Step 3: Recursively invert both subtrees
        # Call invertTree on root.left
        # Call invertTree on root.right
        self.invertTree(root.left)
        self.invertTree(root.right)
        # Step 4: Return
        # Return root (the root of the inverted tree)
        return root
		
		