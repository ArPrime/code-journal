def mergeKListsDivideConquer(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Approach 2: Divide and Conquer
        Time: O(n log k) where n is total nodes, k is number of lists
        Space: O(log k) for recursion stack
        """
        if not lists:
            return None
        
        def mergeTwoLists(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
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
        
        # Divide and conquer
        while len(lists) > 1:
            merged_lists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                merged_lists.append(mergeTwoLists(l1, l2))
            lists = merged_lists
        
        return lists[0] if lists else None