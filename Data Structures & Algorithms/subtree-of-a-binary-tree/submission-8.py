# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    #def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

    def isSameTree(self, root, subRoot):
        # return True if both nodes are None
        if root is None and subRoot is None:
            return True
        # return False if only one node is None
        if root is None or subRoot is None:
            return False
        # return False if node value differs
        if root.val != subRoot.val:
            return False
        return (
            self.isSameTree(root.left, subRoot.left)
            and 
            self.isSameTree(root.right, subRoot.right)
            )


    # Function 2 - is subtree
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # return False if root is None
        if root is None:
            return False
            
        if self.isSameTree(root,subRoot):
            return True

        # return True if isSameTree(root, subroot) is True
        return (
            self.isSubtree(root.left, subRoot)
            or
            self.isSubtree(root.right, subRoot)
        )
