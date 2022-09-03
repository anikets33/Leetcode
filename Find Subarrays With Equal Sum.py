class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        i = 0
        j = 1
        d = {}
        if len(nums)<3:
            return False
        while j<len(nums):
            s = nums[i] + nums[j]
            if s in d:
                return True
            else:
                d[s] = 1
            i += 1
            j += 1
        return False
