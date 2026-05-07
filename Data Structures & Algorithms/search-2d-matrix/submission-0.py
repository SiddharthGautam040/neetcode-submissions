class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for arr in matrix:
            if self.search(arr, target):
                return True
        return False
        

    def search(self, arr: List[int], target: int) -> bool:
        l = 0
        r = len(arr) - 1
        
        while l <= r:

            mid = l + ((r-l) // 2)

            if arr[mid] > target:
                r = mid - 1
            elif arr[mid] < target:
                l = mid + 1
            else:
                return True
        return False