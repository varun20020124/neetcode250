class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0,len(nums)-1
        minimum = math.inf
        while l<=r:
            mid = (l+r)//2
            if nums[mid] >= nums[l]:
                minimum = min(minimum, nums[l])
                l = mid+1
            else:
                minimum = min(minimum, nums[mid])
                r = mid - 1
        return minimum