class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashtb = {}
        res = []
        result = []

        for num in nums:
            hashtb[num] = hashtb.get(num, 0) + 1
        
        for num, freq in hashtb.items():
            res.append([num, freq])
        
        res.sort(key=lambda x : x[1], reverse=True)

        for i in range(k):
            result.append(res[i][0])

        return result
