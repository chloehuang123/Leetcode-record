class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = []
        res.append(intervals[0])

        for i in range(1, len(intervals)):
            pre = res.pop()
            if pre[1] <= intervals[i][0]:
                res.append(pre)
                res.append(intervals[i])
            elif pre[0] >= intervals[i][1]:
                res.append(intervals[i])
                res.append(pre)
            else:
                if pre[1] > intervals[i][1]:
                    res.append(intervals[i])
                else:
                    res.append(pre) 
        return len(intervals) - len(res)
