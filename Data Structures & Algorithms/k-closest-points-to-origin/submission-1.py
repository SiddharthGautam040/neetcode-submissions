class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = []
        heapq.heapify(dist)

        for point in points:
            pt_dist = -(point[0]**2 + point[1]**2)
            heapq.heappush(dist, [pt_dist, point[0], point[1]])
            if len(dist) > k:
                heapq.heappop(dist)


        res = []

        while k > 0:
            ans = heapq.heappop(dist)
            res.append([ans[1], ans[2]])
            k -= 1
        
        return res
