class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
      count = {}
      freq = [[] for i in range(len(nums) + 1)]
      res = []
      for num in nums:
        count[num] = count.get(num, 0) + 1

      for key, val in count.items():
        freq[val].append(key)

      for i in range(len(freq) - 1, -1, -1): 
        while freq[i]:
          if k <= 0:
            return res
          res.append(freq[i].pop())
          k -= 1
          
      
      return res
