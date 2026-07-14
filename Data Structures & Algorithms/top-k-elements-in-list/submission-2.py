
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        arr = [[] for i in range(len(nums)+1)]
        res = []

        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        
        for key, val in freq.items():
            arr[val].append(key)

        for i in range(len(arr)-1, -1, -1):
            while k > 0 and len(arr[i]) > 0:
                res.append(arr[i].pop())
                k = k - 1
        
        return res
            
                
