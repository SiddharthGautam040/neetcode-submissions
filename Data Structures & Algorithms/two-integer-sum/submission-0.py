class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq = {}
        n = len(nums)
        for i in range(n):
          j = target - nums[i]
          if (j) in freq:
            return [freq[j], i]
          else:
            freq[nums[i]] = i
        return None
