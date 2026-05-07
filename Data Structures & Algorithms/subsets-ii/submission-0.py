class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.res = [[]]
        nums.sort()
        self.dfs(nums, [], 0)
        return self.res

    def dfs(self, nums, curr, i):
        if i == len(nums):
            return
        
        curr.append(nums[i])
        self.dfs(nums, curr, i+1)
        self.res.append(curr.copy())
        curr.pop()
        while i < len(nums) - 1 and nums[i] == nums[i + 1]:
            i = i + 1
        self.dfs(nums, curr, i+1)
