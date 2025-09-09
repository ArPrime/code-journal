'''
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

1 <= k <= n <= 5000


Example 1:

Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
'''


from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        
        curr = head
        count = 0
        while curr and count < k:
            curr = curr.next
            count += 1
        
        if count == k:
            next_group_head = self.reverseKGroup(curr, k)

            while count > 0:
                next_temp = head.next
                head.next = next_group_head
                next_group_head = head
                head = next_temp
                count -= 1
            head = next_group_head
            
        return head
    

# # Helper function to reverse a portion of linked list
# def reverseList(self, head: ListNode, tail: ListNode):
#     """
#     Reverses nodes from head to tail (exclusive)
#     Returns new head and tail of reversed portion
#     """
#     prev = tail
#     current = head
    
#     while current != tail:
#         next_temp = current.next
#         current.next = prev
#         prev = current
#         current = next_temp
    
#     return prev, head


# Approach 2: Fast & Slow Pointer (Iterative)
class Solution_2:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head or k == 1:
            return head
        
        # First, check if we have at least k nodes
        fast = head
        for _ in range(k):
            if not fast:
                return head  # Less than k nodes, return as is
            fast = fast.next
        
        # Create dummy node to simplify edge cases
        dummy = ListNode(0)
        dummy.next = head
        prev_group_end = dummy
        
        while True:
            # Find the start and end of current k-group
            group_start = prev_group_end.next
            group_end = prev_group_end
            
            # Move group_end k steps forward
            for _ in range(k):
                group_end = group_end.next
                if not group_end:
                    # Less than k nodes remaining
                    return dummy.next
            
            next_group_start = group_end.next
            
            # Reverse the current k-group
            prev = next_group_start
            current = group_start
            
            # Reverse k nodes
            for _ in range(k):
                next_temp = current.next
                current.next = prev
                prev = current
                current = next_temp
            
            # Connect with previous group
            prev_group_end.next = prev  # prev is now the new head of reversed group
            prev_group_end = group_start  # group_start is now the tail
        
        return dummy.next