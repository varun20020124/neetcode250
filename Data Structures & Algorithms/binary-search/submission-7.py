class Solution:
    def search(self, num: List[int], target: int) -> int:
        l,h = 0,len(num)-1
        while l <= h:
            mid = (l+h)//2
            if num[mid] == target:
                return mid
            elif num[mid] > target:
                h = mid-1
            else:
                l = mid+1
        return -1