"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        startPt = 0
        endPt = 0
        res = 0
        count = 0
        while startPt < len(start):
            if start[startPt] >= end[endPt]:
                endPt += 1
                count -= 1
            else:
                count += 1
                startPt += 1
            res = max(count, res)
        return res