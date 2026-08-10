# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        mid = slow.next
        slow.next = None
        curr = mid
        prev = None

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        
        while head and prev:
            head_next = head.next
            prev_next = prev.next

            head.next = prev
            prev.next = head_next

            prev = prev_next
            head = head_next
        
        return None

        
        
            