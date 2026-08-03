class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0
        for i, v in enumerate(heights):
            start = i
            while stack and stack[-1][1] > v:
                index, val = stack.pop()
                res = max(res, (i - index) * val)
                start = index
            stack.append((start, v))
        
        while stack:
            index, val = stack.pop()
            n = len(heights)
            res = max(res, (n - index) * val)
        
        return res