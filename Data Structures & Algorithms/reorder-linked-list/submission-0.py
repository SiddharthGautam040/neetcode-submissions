# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return None
        mid = head
        fast = head
        dummy = ListNode()
        while fast.next and fast.next.next:
            mid = mid.next
            fast = fast.next.next

        newList = self.reverseList(mid.next)
        mid.next = None
        
    
        while newList and head:
            up_head = head.next
            head.next = newList
            head = up_head
            
            up_newList = newList.next
            newList.next = head
            newList = up_newList

        
        

    
    def reverseList(self, head):
        prev = None
        while head:
            upcoming = head.next
            head.next = prev
            prev = head
            head = upcoming
        return prev

