# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = [root]

        while q:
            lq = len(q)
            val = None
            for i in range(lq):
                ele = q.pop(0)
                if ele:
                    val = ele.val
                    q.append(ele.left)
                    q.append(ele.right)
            if val:
                res.append(val)
        return res
