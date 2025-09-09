'''
Given the head of a singly linked list, reverse the list, and return the reversed list.

 

Example 1:

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
'''


# # 旧语法
# from typing import Optional
# def old_way(param: Optional[str]) -> None:
#     pass

# # 新语法（Python 3.10+）
# def new_way(param: str | None) -> None:
#     pass



class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    @staticmethod
    def reverseList(head: ListNode | None) -> ListNode | None:
        prev = None
        curr = head

        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
        
        return prev

def create_linked_list(arr):
    if not arr:
        return None
    
    head = ListNode(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

def print_linked_list(head):
    result = []
    curr = head
    while curr:
        result.append(str(curr.val))
        curr = curr.next
    return ' -> '.join(result) if result else 'Empty'

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
    
#     def __repr__(self):
#         """Helper method to print the linked list"""
#         result = []
#         curr = self
#         while curr:
#             result.append(str(curr.val))
#             curr = curr.next
#         return " -> ".join(result)

head_1 = create_linked_list(arr=[1, 3, 2])
print(print_linked_list(head_1))
reversed_head_1 = Solution.reverseList(head_1)
print(print_linked_list(reversed_head_1))


node_1 = ListNode(10)
node_2 = ListNode(14)
node_3 = ListNode(12)

node_1.next = node_2
node_2.next = node_3


head_3 = ListNode(1, ListNode(2, ListNode(3)))


print(print_linked_list(Solution.reverseList(node_1)))
print(print_linked_list(Solution.reverseList(head_3)))