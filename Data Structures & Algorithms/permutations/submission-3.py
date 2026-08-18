class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        
        def dfs(curr, nums):
            if len(curr) == n:
                res.append(curr.copy())
                return
            
            for i in range(len(nums)):
                val = nums[i]
                curr.append(val)
                nums.pop(i)
                dfs(curr, nums)
                nums.insert(i, val)
                curr.pop()


        dfs([], nums)

        return res