class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []
        heapq.heapify(self.left)
        heapq.heapify(self.right)

    def addNum(self, num: int) -> None:
        if not self.left:
            heapq.heappush(self.left, num * -1)
            return None

        left_num = self.left[0] * -1
        
        if num < left_num:
            heapq.heappush(self.left, num * -1)
        else:
            heapq.heappush(self.right, num)

        if (len(self.right) + len(self.left)) % 2:
            while len(self.right) >= len(self.left) + 1:
                right_num = heapq.heappop(self.right)
                heapq.heappush(self.left, right_num * -1)
        else:
            while len(self.right) < len(self.left):
                left_num = heapq.heappop(self.left) * -1
                heapq.heappush(self.right,left_num)

    def findMedian(self) -> float:
        if (len(self.right) + len(self.left)) % 2:
            res = self.left[0] * -1
        else:
            res = ((self.left[0] * -1) + (self.right[0])) / 2
        
        return float(res)


                