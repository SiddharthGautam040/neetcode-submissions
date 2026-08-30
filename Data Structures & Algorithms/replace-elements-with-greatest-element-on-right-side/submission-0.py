class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        largest_seen = -1
        n = len(arr) - 1
        for i in range(n, -1, -1):
            curr_ele = arr[i]
            arr[i] = largest_seen
            largest_seen = max(largest_seen, curr_ele)
          
        return arr

