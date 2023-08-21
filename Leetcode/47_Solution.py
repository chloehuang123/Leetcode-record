class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        used = [False] * len(nums)

        def dfs(recorder):
            if len(recorder) == len(nums):
                res.append(recorder[:])
            
            for i in range(len(nums)):
                if used[i] or (i>0 and not used[i-1] and nums[i] == nums[i-1]):
                    continue
                recorder.append(nums[i])
                used[i] = True
                dfs(recorder)
                recorder.pop()
                used[i] = False
        dfs([])
        return res
