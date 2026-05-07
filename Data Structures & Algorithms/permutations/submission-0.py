class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        res = self.permute(nums[1:])
        new_res = []
        for arr in res:
            for i in range(len(arr) + 1):
                curr_c = arr.copy()
                curr_c.insert(i, nums[0])
                new_res.append(curr_c)
        return new_res


    #   [1,2,3] 2,1,3 2,3,1 1,3,2 3,1,2 3,2,1
    #    [2,3] [3,2] 
    #     [[3]]
