class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key= lambda i : i[0])
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            firstInterval = res[-1]

            if firstInterval[1] < intervals[i][0]:
                res.append(intervals[i])
            else:
                res[-1] = [min(firstInterval[0], intervals[i][0]), max(firstInterval[1], intervals[i][1])]

        return res