class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        d = {}
        for each in arr:
            if each in d:
                d[each] += 1
            else:
                d[each] = 1
        n = len(arr)//2
        l = list(d.values())
        l.sort(reverse = True)
        c = 0
        p = 0
        
        for each in l:
            c += 1
            p += each
            if p>=n:
                break
        return c
        
