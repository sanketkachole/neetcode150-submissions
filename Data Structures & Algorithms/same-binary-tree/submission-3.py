# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        # Case 1: Both nodes are empty
        # IF p is None AND q is None:
        #     RETURN True
        if p is None and q is None:
            return True

        # Case 2: Only one node is empty
        # IF p is None OR q is None:
        #     RETURN False
        if p is None or q is None:
            return False

        # Case 3: Node values differ
        # IF p.value != q.value:
        #     RETURN False
        if p.val != q.val:
            return False
            
        # Case 4: Compare left and right subtrees
        # RETURN (
        #     sameTree(p.left, q.left)
        #     AND
        #     sameTree(p.right, q.right)
        # )
        return (
            self.isSameTree(p.left, q.left)
            and
            self.isSameTree(p.right, q.right)
            )

