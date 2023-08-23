class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key= lambda x: x[0])
        res = [intervals[0]]

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
