class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        a = []
        d = {}
        for each in paths:
            a = each.split()
            s = a[0] + '/'
            for i in range(1, len(a)):
                start = a[i].index('(')
                end = a[i].index(')')
                k = a[i][start+1:end]
                if k in d:
                    d[k].append(s+a[i][:start])
                else:
                    d[k] = [s+a[i][:start]]
        l = list(d.values())
        i = 0
        while i<len(l):
            if len(l[i]) == 1:
                del l[i]
            else:
                i += 1
        return l
