class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []

        for num in nums1:
            if num in nums2:
                nums2.remove(num)
                res.append(num)
        return res
