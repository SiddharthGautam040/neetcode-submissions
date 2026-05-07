class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(curr, i, curr_sum):
            if i >= len(nums):
                return            
            if curr_sum > target:
                return
            if curr_sum == target:
                res.append(curr.copy())
                return

            curr.append(nums[i])
            new_sum = curr_sum + nums[i]
            dfs(curr, i, new_sum)
            curr.pop()
            dfs(curr, i+1, curr_sum)
            return
        
        dfs([], 0, 0)
        return res