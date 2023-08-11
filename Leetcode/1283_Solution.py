class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def isPossible(H):
            cal_sum = 0
            for num in nums:
                cal_sum += -(-num // H)
            return cal_sum <= threshold
        
        low = 1
        high = max(nums)

        while low < high:
            mid = (low + high) // 2

            if not isPossible(mid):
                low = mid + 1
            else:
                high = mid
        return high
