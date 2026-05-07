class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        area = 0
        while l < r:
            area = max(min(heights[l], heights[r]) * (r - l), area)
            if heights[l] < heights[r]:
                l = l + 1
            else:
                r = r - 1
        return area