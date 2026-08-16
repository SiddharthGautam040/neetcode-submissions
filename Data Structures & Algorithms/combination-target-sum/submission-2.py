class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        combi = []

        def dfs(i):

            if i >= len(nums) or sum(combi) >= target:
                if sum(combi) == target:
                    res.append(combi.copy())
                return
            
            combi.append(nums[i])
            dfs(i)
            combi.pop()
            dfs(i+1)
        
        dfs(0)
        return res
        
