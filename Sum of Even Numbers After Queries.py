class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ans = [0]*(len(nums))
        
        even = 0
        for x in nums:
            if x%2 == 0:
                even += x 
        
        for i, each in enumerate(queries):
            a = nums[each[1]]
            t = a+each[0]
            if t%2 == 0:
                even += t
            if a%2 == 0:
                even -= a
            nums[each[1]] = t
            ans[i] = even
        
        return ans
        
