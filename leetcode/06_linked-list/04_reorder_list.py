'''
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

 

Example 1:

Input: head = [1,2,3,4]
Output: [1,4,2,3]
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        slow = fast = head
        first_half_end = None
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second_half = reverseList(slow.next)
        slow.next = None
        first_half = head

        while second_half:
            first_next = first_half.next
            second_next = second_half.next

            first_half.next = second_half
            second_half.next = first_next

            first_half = first_next
            second_half = second_next


def reverseList(head: ListNode | None) -> ListNode | None:
    prev = None
    curr = head

    while curr:
        next_temp = curr.next
        curr.next = prev
        prev = curr
        curr = next_temp
    
    return prev


# def reorderList_array(self, head):
#     """
#     思路：
#     1. 遍历链表，把所有节点存到数组中
#     2. 用双指针交替取节点重新连接
#     3. 时间O(n)，空间O(n)
#     """
#     if not head or not head.next:
#         return
    
#     # 步骤1：收集所有节点到数组
#     nodes = []
#     curr = head
#     while curr:
#         nodes.append(curr)
#         curr = curr.next
    
#     # 步骤2：双指针交替重连
#     left, right = 0, len(nodes) - 1
    
#     while left < right:
#         # 连接 left -> right
#         nodes[left].next = nodes[right]
#         left += 1
        
#         if left == right:  # 防止偶数个节点时重复连接
#             break
            
#         # 连接 right -> left
#         nodes[right].next = nodes[left]
#         right -= 1
    
#     # 最后一个节点的next置空
#     nodes[left].next = None