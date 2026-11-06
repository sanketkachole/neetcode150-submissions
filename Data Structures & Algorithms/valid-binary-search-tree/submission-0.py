# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        previous = None

        def dfs(node):
            nonlocal previous
            if node is None:
                return True
                
            if not dfs(node.left):
                return False
            
            if previous is not None and node.val <= previous:
                return False
            previous = node.val
            return dfs(node.right)
            
        return dfs(root)





        