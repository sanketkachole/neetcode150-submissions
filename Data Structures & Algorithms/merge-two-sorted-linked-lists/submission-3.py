# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # # Handle empty lists
        # if list1 is None:
        #     return list2
        # if list2 is None:
        #     return list1

        # # Initialize pointers
        # pointer1 = list1
        # pointer2 = list2
        # merged_head = None
        # tail = None

        # # Compare nodes while both lists have nodes
        # while pointer1 is not None and pointer2 is not None:

        #     # Select smaller node and advance its pointer
        #     if pointer1.val < pointer2.val:
        #         selected_node = pointer1
        #         pointer1 = pointer1.next
        #     else:
        #         selected_node = pointer2
        #         pointer2 = pointer2.next

        #     # Initialize merged list only once
        #     if merged_head is None:
        #         merged_head = selected_node
        #         tail = selected_node
        #     else:
        #         # Connect selected node
        #         tail.next = selected_node

        #         # Advance tail
        #         tail = selected_node

        # # Attach remaining nodes
        # if pointer1 is not None:
        #     tail.next = pointer1
        # else:
        #     tail.next = pointer2

        # # Return head of merged list
        # return merged_head








        if list1 is None and list2 is None:
            return None
        elif list1 is None and list2 is not None:
            return list2
        elif list1 is not None and list2 is None:
            return list1

        if list1.val < list2.val:
            head = list1
            tail = list1
            list1 = list1.next
            
        else:
            head = list2
            tail = list2
            list2 = list2.next
            
        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                temp = list1.next
                tail.next = list1
                tail = list1
                list1 = temp
                
            else:
                temp = list2.next
                tail.next = list2
                tail = list2
                list2 = temp

        tail.next = list2 if list1 is None else list1

        return head


