"""
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
"""


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        length = m + n
        m -= 1
        n -= 1

        while n >= 0:
            length -= 1
            if m >= 0 and nums1[m] > nums2[n]:
                nums1[length] = nums1[m]
                m -= 1
            else:
                nums1[length] = nums2[n]
                n -= 1
