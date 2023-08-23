class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        res.append(newInterval)

        for interval in intervals:
            pre = res.pop()

            if pre[1] < interval[0]:
                res.append(pre)
                res.append(interval)
            elif pre[0] > interval[1]:
                res.append(interval)
                res.append(pre)
            else:
                res.append([min(pre[0], interval[0]), max(pre[1], interval[1])])
        
        return res
