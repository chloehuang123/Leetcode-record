class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check_time(H):
            time = 0
            for item in piles:
                time += -(-item // H)
            return time <= h

        low = 1
        high = max(piles)

        while low < high:
            mid = (low + high) // 2
            if not check_time(mid):
                low = mid + 1
            else:
                high = mid
        return high
