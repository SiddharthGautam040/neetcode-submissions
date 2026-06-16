class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}

        def dfs(i, curr_sum):
            if i >= len(nums):
                if curr_sum == target:
                    return 1
                else:
                    return 0
            if (i, curr_sum) in dp:
                return dp[(i, curr_sum)]
            add = dfs(i + 1, curr_sum + nums[i])
            sub = dfs(i + 1, curr_sum - nums[i])
            dp[(i, curr_sum)] = add + sub
            return dp[(i, curr_sum)]
        return dfs(0, 0)