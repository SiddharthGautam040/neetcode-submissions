class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxi = 1
        mini = 1
        res = nums[0]
        for i in nums:
            temp = maxi * i
            maxi = max(maxi * i, i, mini * i)
            mini = min(mini * i, i, temp)
            res = max(res, maxi)
        return res
                
            