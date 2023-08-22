class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def dfs(i, target, recorder):
            if target == 0:
                res.append(recorder[:])
            if target < 0:
                return
            
            for j in range(i, len(candidates)):
                if j>i and candidates[j] == candidates[j-1]:
                    continue
                recorder.append(candidates[j])
                dfs(j+1, target-candidates[j], recorder)
                recorder.pop()

        dfs(0, target, [])
        return res
