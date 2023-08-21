class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        def dfs(i, recorder):
            for j in range(i, len(nums)):
                recorder.append(nums[j])
                res.append(recorder[:])
                dfs(j+1, recorder)
                recorder.pop()
        dfs(0, [])
        return res
