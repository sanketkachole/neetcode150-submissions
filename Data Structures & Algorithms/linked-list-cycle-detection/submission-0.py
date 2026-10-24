# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Initialize slow and fast pointers at head.
        pointer1 = head
        pointer2 = head

        # Repeat while the fast pointer and its next reference are both not None:
        while pointer2 is not None and pointer2.next is not None:

            # Move slow pointer one node forward.
            pointer1 = pointer1.next
            # Move fast pointer two nodes forward.
            pointer2 = pointer2.next.next
            # If both pointers reference the same node:
                # Return True.
            if pointer1 is pointer2:
                return True
        # If the loop finishes without the pointers meeting:
        # Return False.
        return False




