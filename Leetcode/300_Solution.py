class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        stack = [nums[0]]

        for i in range(1, len(nums)):
            if nums[i] > stack[-1]:
                stack.append(nums[i])
            else:
                j = 0
                while stack[j] < nums[i]:
                    j += 1
                stack[j] = nums[i]
        return len(stack)
