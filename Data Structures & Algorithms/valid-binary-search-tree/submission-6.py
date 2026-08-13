# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return (True, float("inf"), float("-inf"))
            
            is_left_valid, lmi, lmx = dfs(root.left)
            is_right_valid, rmi, rmx = dfs(root.right)

            if (is_left_valid and is_right_valid) and lmx < root.val < rmi:
                return (True, min(lmi, root.val), max(rmx, root.val))
            else:
                return (False, min(lmi, root.val), max(rmx, root.val))

        return dfs(root)[0]
        
  