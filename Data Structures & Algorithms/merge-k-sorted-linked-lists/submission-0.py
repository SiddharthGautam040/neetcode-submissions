# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        while len(lists) > 1:
            write = 0
            for i in range(0, len(lists) - 1, 2):
                lists[write] = self.merge(lists[i], lists[i+1])
                write += 1
            
            if len(lists) % 2:
                lists[write] = lists[-1]
                write += 1
            
            lists = lists[0:write]
        
        return lists[0] if lists else None
        
    def merge(self, l1, l2):
        dummy = ListNode()
        merged = dummy
        while l1 and l2:
            if l1.val < l2.val:
                merged.next = l1
                l1 = l1.next
            else:
                merged.next = l2
                l2 = l2.next
            merged = merged.next
        
        while l1:
            merged.next = l1
            l1 = l1.next
            merged = merged.next

        
        while l2:
            merged.next = l2
            l2 = l2.next
            merged = merged.next

        
        return dummy.next
