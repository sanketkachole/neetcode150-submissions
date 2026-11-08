# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        # Create a hash map of inorder values and their indices
        index_map = {}
        for i, value in enumerate(inorder):
            index_map[value] = i

        # Initialize the preorder index
        preorder_index = 0

        # Define the recursive function
        def build(left, right):
            nonlocal preorder_index

            # Base case: empty subtree
            if left > right:
                return None

            # Select the next root from preorder
            root_value = preorder[preorder_index]
            preorder_index += 1

            # Create the root node
            root = TreeNode(root_value)

            # Find the root's position in inorder
            root_index = index_map[root_value]

            # Recursively construct and attach the left subtree
            root.left = build(left, root_index - 1)

            # Recursively construct and attach the right subtree
            root.right = build(root_index + 1, right)

            # Return the constructed subtree root
            return root

        # Construct the entire tree and return its root
        return build(0, len(inorder) - 1)





