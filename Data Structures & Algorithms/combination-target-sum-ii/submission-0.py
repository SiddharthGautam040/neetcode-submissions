class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(curr, i , curr_sum):
            if curr_sum == target:
                res.append(curr.copy())
                return

            if i >= len(candidates) or curr_sum > target:
                return

            curr.append(candidates[i])
            new_sum = curr_sum + candidates[i]
            dfs(curr, i + 1, new_sum)
            curr.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i = i + 1
            dfs(curr, i + 1, curr_sum)

        
        dfs([], 0, 0)
        return res