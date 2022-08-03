class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq = {}
        for i in range(len(nums)):
            x = target-nums[i]
            if x in freq:
                return [freq[x], i]
            else:
                freq[nums[i]] = i
                
