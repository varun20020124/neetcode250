class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        quads = set()
        for i in range(len(nums)-3):
            for j in range(i+1,len(nums)-2):
                left = j+1
                right = len(nums)-1
                while left < right:
                    four_sum = nums[i]+nums[j]+nums[left]+nums[right]
                    if four_sum > target:
                        right-=1
                    elif four_sum < target:
                        left+=1
                    else:
                        quads.add((nums[i],nums[j],nums[left],nums[right]))
                        left+=1
        result = []
        for tup in quads:
            result.append(list(tup))
        return result