class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
      numSet = set(nums)
      res = 0
      for num in nums:
        length = 0
        if num - 1 in numSet:
          length = 0
        curr = num
        while curr in numSet:
          curr += 1
          length += 1
        res = max(length, res)
      
      return res