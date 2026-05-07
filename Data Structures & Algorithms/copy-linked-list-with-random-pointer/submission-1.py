"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCopy = {}

        curr = head
        while curr:
            oldToCopy[curr] = Node(x=curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            new = oldToCopy[curr]
            new.next = oldToCopy.get(curr.next)
            new.random = oldToCopy.get(curr.random)
            curr = curr.next

        return oldToCopy.get(head)