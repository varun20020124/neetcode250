class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        j = max(nums)
        if j <= 0:
            return 1
        for num in range(1,j):
            if num not in nums:
                return num
        return j+1