class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0 for i in range(len(temperatures))]

        for idx, temp in enumerate(temperatures):
            val = (idx, temp)
            while stack and temp > stack[-1][1]:
                item = stack.pop()
                res[item[0]] = idx - item[0]
            stack.append(val)
        return res