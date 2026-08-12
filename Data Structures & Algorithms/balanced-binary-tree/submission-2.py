# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        stack = [root]
        mp = {}
        res = []

        while stack:
            node = stack.pop()
            res.append(node)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)


        for node in reversed(res):
            left = mp.get(node.left, 0)
            right = mp.get(node.right, 0)

            mp[node] = 1 + max(left, right)
            if abs(left - right) > 1:
                return False
        
        return True
