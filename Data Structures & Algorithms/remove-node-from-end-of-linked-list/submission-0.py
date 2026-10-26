# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    
        # Step 1: Reverse the original linked list
        # Initialize previous as None and current as head
        previous = None
        current = head
        # While current is not None:
        while current is not None:
            # Save the next node in temporary
            temporary = current.next
            # Change current's next reference to previous
            current.next = previous
            # Move previous to current
            previous = current
            # Move current to temporary
            current = temporary
        # Store previous as the reversed list's head
        reverse_list_head = previous

        # Step 2: Find the nth node in the reversed list
        # Initialize current at the reversed head
        previous = None
        current = reverse_list_head
        # Initialize previous as None
        previous = None
        # Initialize counter to 1
        counter = 1
        # While counter is less than n:
        while counter < n:
            # Move previous to current
            previous = current
            # Move current to the next node
            current = current.next
            # Increase counter by 1
            counter += 1

        # Step 3: Remove the nth node
        # If previous is None:
        if previous is None:
            # Move the reversed head to current's next node
            reverse_list_head = current.next
        # Otherwise:
        else:
            # Connect previous directly to current's next node
            previous.next = current.next
        # Step 4: Reverse the remaining linked list again
        # Use the same reversal procedure from Step 1
        # While current is not None:
        previous = None
        current = reverse_list_head
        while current is not None:
            # Save the next node in temporary
            temporary = current.next
            # Change current's next reference to previous
            current.next = previous
            # Move previous to current
            previous = current
            # Move current to temporary
            current = temporary
        # Store previous as the reversed list's head
        reverse_list_head_again = previous
        # Return the new head
        return reverse_list_head_again



