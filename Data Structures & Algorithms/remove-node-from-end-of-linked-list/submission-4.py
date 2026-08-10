# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        prev = dummy
        curr = dummy.next
        fast = curr

        while n > 0:
            fast = fast.next
            n = n - 1

        while fast:
            fast = fast.next
            curr = curr.next
            prev = prev.next
        
        prev.next = curr.next

        return dummy.next