# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float("-inf")
        
        def postorder(root):
            nonlocal res
            if not root:
                return 0

            l = postorder(root.left)
            r = postorder(root.right)

            max_ex_p = root.val + max(l, r, 0)
            max_inc_p = root.val + l + r
            res = max(res, max_ex_p, max_inc_p)

            return max_ex_p
        postorder(root)
        return res



        # stack = []
        # mp = {}
        # curr = root
        # res = float("-inf")
        # while stack or curr:
        #     while curr:
        #         stack.append(curr)
        #         curr = curr.left

        #     curr = stack.pop()

        #     l = mp.get(curr.left, 0)
        #     r = mp.get(curr.right, 0)

        #     max_ex_p = curr.val + max(l, r)
        #     max_inc_p = curr.val + l + r
        #     print(curr.val)
        #     mp[curr] = max_ex_p
        #     res = max(mp[curr], max_inc_p)

        #     right = curr.right
        #     curr = right
                
        # return res
            
            