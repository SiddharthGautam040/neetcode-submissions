# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue1 = [p]
        queue2 = [q]

        while queue1 and queue2:
            ele1 = queue1.pop(0)
            ele2 = queue2.pop(0)

            if ele1 is None and ele2 is None:
                continue
            elif ele1 and not ele2:
                return False
            elif ele2 and not ele1:
                return False
            elif ele1.val != ele2.val:
                return False
            queue1.append(ele1.left)
            queue2.append(ele2.left)
            queue1.append(ele1.right)
            queue2.append(ele2.right)
        
        return False if queue1 or queue2 else True