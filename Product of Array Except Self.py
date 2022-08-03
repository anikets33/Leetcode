class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [nums[0]]
        suffix = [nums[-1]]
        
        for i in range(1, len(nums)):
            prefix.append(nums[i]*prefix[i-1])
            suffix.append(nums[len(nums)-i-1]*suffix[i-1])
        
        prefix.insert(0, 1)
        suffix.insert(0, 1)
        
        result = []
        
        for i in range(len(nums)):
            result.append(prefix[i]*suffix[len(nums)-i-1])
        
        return result
