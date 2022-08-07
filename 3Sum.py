class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        
        def twoSum(arr, target, first):
            i, j, prev = 0, len(arr)-1, math.inf
            while i<j:
                if arr[i] + arr[j] == target and arr[i] != prev:
                    ans.append([first, arr[i], arr[j]])
                    prev = arr[i]
                    i += 1
                    j -= 1
                elif arr[i] + arr[j] < target:
                    i += 1
                else:
                    j -= 1
            return
        
        prev = math.inf
        for i in range(len(nums)-2):
            #try to use binary search to find last occurence
            if nums[i] != prev:
                twoSum(nums[i+1:], 0-nums[i], nums[i])
            prev = nums[i]
        return ans
