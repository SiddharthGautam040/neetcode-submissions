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
        oldToNew = {}

        old_head = head

        while head:
            oldToNew[head] = oldToNew.get(head, Node(head.val) if head else None)

            oldToNew[head.next] = oldToNew.get(head.next, Node(head.next.val) if head.next else None)
            oldToNew[head.random] = oldToNew.get(head.random, Node(head.random.val) if head.random else None)
            new_head = oldToNew[head]
            new_head.next = oldToNew[head.next]
            new_head.random = oldToNew[head.random]
            head = head.next
    
        return oldToNew[old_head] if old_head else None
            