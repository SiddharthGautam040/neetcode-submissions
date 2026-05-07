class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in nums:
            count[i] = 1 + count.get(i, 0)

        n = len(nums)
        arr = [list() for i in range(n + 1)]

        for key, value in count.items():
            arr[value].append(key)

        res = []
        for i in range(len(arr) - 1, 0, -1):
            for j in arr[i]:
                res.append(j)
                if len(res) == k:
                    return res
        return res
