class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l = []
        d = {}
        for each in nums1:
            if each in d:
                d[each] += 1
            else:
                d[each] = 1
        for each in nums2:
            if each in d and d[each]>0:
                d[each] -= 1
                l.append(each)
        return l
