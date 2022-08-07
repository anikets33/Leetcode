class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        a = set(nums1)
        b = set(nums2)
        
        d = {}
        ans = []
        
        for each in a:
            d[each]=1
        for each in b:
            if each in d:
                d.pop(each)
            else:
                ans.append(each)
        
        return [d.keys(), ans]
