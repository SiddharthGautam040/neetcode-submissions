# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if q and p:
            q1 = deque([q])
            q2 = deque([p])
        else:
            if not q and not p:
                return True
            else:
                return False

        while q1 and q2:
            node1 = q1.popleft()
            node2 = q2.popleft()

            if (node1 and node2 and node1.val != node2.val) or (node1 and not node2) or (not node1 and node2):
                return False

            if node1:
                q1.append(node1.left)
                q1.append(node1.right)
            
            if node2:
                q2.append(node2.left)
                q2.append(node2.right)

        return True
            


        