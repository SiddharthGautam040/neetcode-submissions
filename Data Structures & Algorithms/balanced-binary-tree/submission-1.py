# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        _, height = self.height(root)
        return _
    
    def height(self, root):
        if not root: return (True, 0)

        _, left_height = self.height(root.left)
        if _ is False: return (False, 0) 
        _, right_height = self.height(root.right)
        if _ is False: return (False, 0)

        if abs(left_height - right_height) > 1:
            return (False, 0)
        
        return (True, 1 + max(left_height, right_height))