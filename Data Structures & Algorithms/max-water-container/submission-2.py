class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0

        l = 0
        r = len(heights) - 1

        while l < r:
            minH = min(heights[l], heights[r])
            res = max(res, minH * (r - l))

            if heights[l] > heights[r]:
                r = r - 1
            else:
                l = l + 1
        return res
