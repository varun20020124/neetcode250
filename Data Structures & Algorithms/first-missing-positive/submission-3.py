class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = set(nums)
        for num in range(1, len(nums)+2):
            if num not in nums:
                return num