'''
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

0 <= lists.length <= 104
0 <= lists[i].length <= 500


Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
'''


from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    @staticmethod
    def _merge_two_lists(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
            dummy = ListNode(0)
            curr = dummy
            
            while l1 and l2:
                if l1.val <= l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                curr = curr.next
            
            # Attach remaining nodes
            curr.next = l1 or l2
            return dummy.next
    
    @staticmethod
    def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
             return None
        while len(lists) > 1:
             merged_lists = []
             for i in range(0, len(lists), 2):
                  l1 = lists[i]
                  l2 = lists[i + 1] if i + 1< len(lists) else None
                  merged_lists.append(Solution._merge_two_lists(l1, l2))
             lists = merged_lists
        return lists[0] if lists else None


# import heapq
# from typing import List, Optional

# class Solution:
#     def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
#         """
#         Approach 1: Min Heap (Priority Queue)
#         Time: O(n log k) where n is total nodes, k is number of lists
#         Space: O(k) for the heap
#         """
#         if not lists:
#             return None
        
#         # Min heap to store (value, index, node)
#         heap = []
        
#         # Initialize heap with first node from each non-empty list
#         for i, node in enumerate(lists):
#             if node:
#                 heapq.heappush(heap, (node.val, i, node))
        
#         dummy = ListNode(0)
#         curr = dummy
        
#         while heap:
#             val, i, node = heapq.heappop(heap)
#             curr.next = node
#             curr = curr.next
            
#             # Add next node from the same list if exists
#             if node.next:
#                 heapq.heappush(heap, (node.next.val, i, node.next))
        
#         return dummy.next