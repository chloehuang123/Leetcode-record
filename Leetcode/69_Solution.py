class Solution:
    def mySqrt(self, x: int) -> int:
        # x = 0 or 1 时返回结果

        if x <= 1:
            return x
        
        l, r = 1, x

        while l <= r:
            mid = (r + l ) // 2

            if mid ** 2 == x:
                return mid
            elif mid ** 2 <= x:
                l = mid + 1
            else:
                r = mid - 1
        return r
