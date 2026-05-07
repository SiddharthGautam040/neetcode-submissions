"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return node
        q = deque([node])
        root = node
        oldToNew = {}
        while q:
            curr_node = q.popleft()
            if curr_node not in oldToNew:
                oldToNew[curr_node] = Node(curr_node.val)
            
            for nei in curr_node.neighbors:
                if nei not in oldToNew:
                    q.append(nei)
                    oldToNew[nei] = Node(nei.val)
                oldToNew[curr_node].neighbors.append(oldToNew[nei])

        return oldToNew[root]
            

            

            
