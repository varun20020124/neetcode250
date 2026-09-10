class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        res = [0] * (len(nums1) + len(nums2))

        i = len(nums1) - 1
        j = len(nums2) - 1
        write = len(res) - 1

        # Both arrays still have elements
        while i >= 0 and j >= 0:
            if nums1[i] >= nums2[j]:
                res[write] = nums1[i]
                i -= 1
            else:
                res[write] = nums2[j]
                j -= 1

            write -= 1

        # Remaining nums1 elements
        while i >= 0:
            res[write] = nums1[i]
            i -= 1
            write -= 1

        # Remaining nums2 elements
        while j >= 0:
            res[write] = nums2[j]
            j -= 1
            write -= 1

        n = len(res)

        if n % 2 != 0:
            return res[n // 2]
        else:
            return (res[n // 2] + res[n // 2 - 1]) / 2