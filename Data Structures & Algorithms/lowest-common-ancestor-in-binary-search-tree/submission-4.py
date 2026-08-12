# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.lca = None
        self.dfs(root, p, q)
        return self.lca

    def dfs(self, root, p, q):
        if not root:
            return None

        left_has_it = self.dfs(root.left, p, q)
        right_has_it = self.dfs(root.right, p, q)

        if (left_has_it and right_has_it):
            self.lca = root
            return True

        if (root.val == p.val or root.val == q.val) and (left_has_it or right_has_it):
            self.lca = root
            return True

        if (root.val == p.val or root.val == q.val):
            return True
        
        if (left_has_it or right_has_it):
            return True
        
