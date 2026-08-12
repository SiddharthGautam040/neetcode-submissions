# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        mp = {root: (0, 0, 0)}
        stack = [root]
        res = []
        
        while stack:
            node = stack.pop()
            res.append(node)

            if node.left:
                stack.append(node.left)
        
            if node.right:
                stack.append(node.right)

        
        diameter = 0

        for node in reversed(res):
            left = mp.get(node.left, 0)
            right = mp.get(node.right, 0)

            mp[node] = 1 + max(left, right)
            diameter = max(diameter, left + right)

        return diameter
