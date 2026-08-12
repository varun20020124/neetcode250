class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = set()
        for i in range(len(nums)-2):
            j = i+1
            k = len(nums)-1
            while j < k:
                three_sum = nums[i] + nums[j] + nums[k]
                if three_sum > 0:
                    k-=1
                elif three_sum < 0:
                    j+=1
                else:
                    triplets.add((nums[i],nums[j],nums[k]))
                    j+=1
        result = []
        for tup in triplets:
            result.append(list(tup))
        return result