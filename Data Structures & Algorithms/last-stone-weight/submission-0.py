class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)

        while len(stones) >= 2:
            x = heapq.heappop_max(stones)
            y = heapq.heappop_max(stones)

            diff = abs(x-y)
            if diff == 0:
                continue
            else:
                heapq.heappush_max(stones, diff)
        
        res = 0
        if stones:
            res = heapq.heappop_max(stones)
        return res