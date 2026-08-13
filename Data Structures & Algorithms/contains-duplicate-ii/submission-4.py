class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap = defaultdict(list)
        for i in range(len(nums)):
            if nums[i] not in hashmap:
                hashmap[nums[i]].append(i)
            else:
                if abs(i-hashmap[nums[i]][-1]) <= k:
                    return True
                hashmap[nums[i]].append(i)
        return False