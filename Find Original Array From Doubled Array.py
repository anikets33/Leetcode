class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed.sort()
        d = Counter(changed)
        l = []
        for each in changed:
            if each == 0:
                if each in d and d[each]%2 != 0:
                    return []
            elif d[each] != 0:
                if each*2 in d and d[each*2] > 0:
                    d[each*2] -= 1
                    d[each] -= 1
                    l.append(each)
                else:
                    return []
        r = []
        if 0 in d:
            k = d[0]//2
            r = [0]*k
        return l+r
