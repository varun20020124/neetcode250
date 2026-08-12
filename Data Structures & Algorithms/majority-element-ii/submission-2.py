class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = defaultdict(int)
        result = []
        n = len(nums)
        for num in nums:
            count[num] += 1
            if count[num] > n//3 and num not in result:
                result.append(num)
        return result 