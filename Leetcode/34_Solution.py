class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = []
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                range_l = mid
                range_r = mid

                while range_l >= 0 and nums[range_l] == target:
                    range_l -= 1
                res.append(range_l + 1)

                while range_r <= len(nums) - 1 and nums[range_r] == target:
                    range_r += 1
                res.append(range_r - 1)

                return res

            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return [-1, -1]
