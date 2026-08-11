class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)//2
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
            if count[num] > n:
                return num