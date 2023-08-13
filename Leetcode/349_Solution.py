class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_set = set(nums1)
        nums2_set = set(nums2)
        res = []

        for num in nums1_set:
            if num in nums2:
                res.append(num)
        return res
