class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for index, value in enumerate(temperatures):
            if not stack:
                stack.append([index, value])
            else:
                while stack and stack[-1][1] < value:
                    ele = stack.pop()
                    res[ele[0]] = index - ele[0]
                stack.append([index, value])
        return res
