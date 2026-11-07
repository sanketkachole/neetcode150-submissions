# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        counter = 0
        answer = None

        def dfs(node):

            nonlocal counter, answer
            
            if node is None or answer is not None:
                return
            
            dfs(node.left)

            if answer is not None:
                return
                
            counter += 1
            
            if counter == k:
                answer =  node.val
                return 
            dfs(node.right)
            
            
        dfs(root)
        return answer
