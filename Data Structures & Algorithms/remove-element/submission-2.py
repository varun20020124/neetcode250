class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        write = 0
        read = 0
        while read < len(nums):
            if val!=nums[read]:
                nums[write] = nums[read]
                write+=1
            read+=1
        return write