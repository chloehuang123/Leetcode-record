class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def dfs(i, target, recorder):
            if target < 0:
                return
            if target == 0:
                res.append(recorder[:])
            for j in range(i, len(candidates)):
                recorder.append(candidates[j])
                dfs(j, target - candidates[j], recorder)
                recorder.pop()

        dfs(0, target, [])
        return res
