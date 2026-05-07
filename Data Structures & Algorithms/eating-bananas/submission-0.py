class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        min_speed = r

        while l <= r:
            mid = (r + l) // 2
            curr_speed = 0
            
            for i in piles:
                curr_speed += math.ceil(i / mid)
            
            if curr_speed <= h:
                min_speed = mid
                r = mid - 1
            else:
                l = mid + 1

        return min_speed
            