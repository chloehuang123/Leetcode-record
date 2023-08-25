class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ht = {}

        for num in nums:
            ht[num] = ht.get(num, 0) + 1

        return [key for key, value in ht.items() if value >= 2]

