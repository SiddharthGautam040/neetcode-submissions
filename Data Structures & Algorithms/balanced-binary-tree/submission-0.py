# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        res = True
        
        def bfs(root):
            nonlocal res
            if not root:
                return 0
            
            lh = bfs(root.left)
            rh = bfs(root.right)
            if abs(lh - rh) > 1:
                res = False

            return 1 + max(lh, rh)
        bfs(root)
        return res