# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # # Initialize pointers
        # previous = None
        # current = head

        # # Continue until all nodes are reversed
        # while current is not None:

        #     # 1. Save the next node
        #     temporary = current.next

        #     # 2. Reverse the reference (your main mistake)
        #     current.next = previous

        #     # 3. Move previous to current
        #     previous = current

        #     # 4. Move current to the saved next node
        #     current = temporary

        # # Return the new head
        # return previous

        # if head is None:
        #     return None
            
        # prev = None
        # current = head

        # while current.next is not None: 
        #     next_node = current.next
        #     prev = current.next              
        #     current.next = next_node.next		 
        #     prev.next = head
        #     head = prev   
        # return head


        if head is None:
            return None
        current = head

        while current.next is not None:
            # first reverse the list
            next_node = current.next.next    # here we declare next node should be 3 we store in next 
            previous = current.next 	# here we say previous node should be 2 we store in previous
            current.next = next_node		# we update next reference of 1 into 3 so it will be 1->3. 1 is connected to 3
            previous.next = head			# here we update the previous node's next reference to 1. 
            head = previous

        return head
        