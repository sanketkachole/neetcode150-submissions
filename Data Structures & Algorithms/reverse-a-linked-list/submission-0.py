# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize pointers
        previous = None
        current = head

        # Continue until all nodes are reversed
        while current is not None:

            # 1. Save the next node
            temporary = current.next

            # 2. Reverse the reference (your main mistake)
            current.next = previous

            # 3. Move previous to current
            previous = current

            # 4. Move current to the saved next node
            current = temporary

        # Return the new head
        return previous