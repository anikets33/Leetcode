class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i, j = 0, k
        
        s = sum(nums[i:j])
        m = s/k

        while j < len(nums):
            s = s - nums[i] + nums[j]
            if s/k > m:
                m = s/k
            i += 1
            j += 1
        
        return m
