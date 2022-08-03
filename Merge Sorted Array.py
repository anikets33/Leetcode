class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j, zero = m-1, n-1, m+n-1
        while i>=0 and j>=0:
            if nums1[i] <= nums2[j]:
                nums1[zero] = nums2[j]
                j -= 1
                zero -= 1
            else:
                nums1[zero] = nums1[i]
                zero -= 1
                i -= 1
        
        while zero>=0:
            if i<0:
                nums1[zero] = nums2[j]
                j -= 1
                zero -= 1
            if j<0:
                nums1[zero] = nums1[i]
                i -= 1
                zero -= 1
