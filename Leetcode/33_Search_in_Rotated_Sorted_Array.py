"""
如果 [l, mid - 1] 是有序数组，且 target 的大小满足 ([nums[l],nums[mid])则我们应该将搜索范围缩小至 [l, mid - 1]，否则在 [mid + 1, r] 中寻找。
如果 [mid, r] 是有序数组，且 target 的大小满足 (nums[mid+1],nums[r])，则我们应该将搜索范围缩小至 [mid + 1, r]，否则在 [l, mid - 1] 中寻找。

"""



class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) -1 

        while l <= r:
            mid = (l +r) // 2

            if target == nums[mid]:
                return mid

            if nums[l] <= nums[mid]:
                
                if target >= nums[l] and target <= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if target >= nums[mid] and target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1 
