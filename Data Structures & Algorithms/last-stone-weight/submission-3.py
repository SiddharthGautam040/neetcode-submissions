class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-1*i for i in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            a = heapq.heappop(stones) * -1
            b = heapq.heappop(stones) * -1
            r = abs(a-b)
            if r: heapq.heappush(stones, r * -1)
        if stones:
            return heapq.heappop(stones) * -1
        else:
            return 0