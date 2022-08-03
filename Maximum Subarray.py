class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        m, mth = -math.inf, 0
        j = 0
        while j<len(nums):
            mth += nums[j]
            m = max(mth, m)
            if mth<0:   mth = 0
            j += 1
        return m
