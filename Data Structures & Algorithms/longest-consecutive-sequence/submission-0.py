class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        res = 0
        for i in nums:
            if i - 1 not in numSet:
                curr = i
                streak = 0
                while curr in numSet:
                    streak += 1
                    curr += 1
                res = max(streak, res)
        return res
                