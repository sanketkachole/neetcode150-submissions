# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
                
        # Handle empty lists
        if head is None or head.next is None:
            return

        # find the middle using slow and fast pointers, then split the list
        # initiate the variables
        pointer1 = head
        pointer2 = head

        while pointer2.next is not None and pointer2.next.next is not None:
            pointer1 = pointer1.next
            pointer2 = pointer2.next.next
            
        central_node = pointer1
            
            
        # Reverse the second half by changing .next references
        previous = None
        current = central_node.next
        central_node.next = None


        while current is not None:
            temporary = current.next
            current.next = previous
            previous = current
            current = temporary
            
        reversed_second_half = previous

        pointer1 = head
        pointer2 = reversed_second_half

        while pointer2 is not None:

            temp1 = pointer1.next
            temp2 = pointer2.next

            pointer1.next = pointer2
            pointer2.next = temp1
            pointer1 = temp1
            pointer2 = temp2

