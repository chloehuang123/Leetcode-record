class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        tempArr = []

        for interval in intervals:
            tempArr.append([interval[0], 1])
            tempArr.append([interval[1], -1])
        
        tempArr.sort(key=lambda x: (x[0], x[1]))

        temp = 0
        res = 0

        for time, value in tempArr:
            temp += value
            res = max(temp, res)
        
        return res
