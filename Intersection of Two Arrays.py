class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a = set(nums1)
        b = set(nums2)
        l = []
        for each in b:
            if each in a:
                l.append(each)
                
        return l
