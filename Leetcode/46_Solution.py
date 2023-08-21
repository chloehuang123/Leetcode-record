class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = [False] * len(nums)

        def dfs(recorder):
            if len(recorder) == len(nums):
                res.append(recorder[:])
            
            for i in range(len(nums)):
                if used[i]:
                    continue
                recorder.append(nums[i])
                used[i] = True
                dfs(recorder)
                recorder.pop()
                used[i] = False
        dfs([])
        return res
