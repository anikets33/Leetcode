class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def permutation(arr, ans):            
            
            if len(arr)==1:
                ans.append(arr[0])
                res.append(ans)
                return 
            
            for i,each in enumerate(arr):
                temp = []
                temp.extend(ans)
                temp.append(each)
                permutation(arr[:i]+arr[i+1:], temp)
            
        permutation(nums, [])
        
        return res
