class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        d = {}
        for i in range(10):
            d[str(i)] = set()
            if i-k>-1:
                d[str(i)].add(str(i-k))
            if i+k<10:
                d[str(i)].add(str(i+k))
        res = []
        
        def createNum(i, s):
            if i == 1:
                res.append(s)
                return 
            
            l = d[s[-1]]
            for each in l:
                t = s+each
                createNum(i-1, t)
            
            return 
        
        for j in range(1, 10):
            if len(d[str(j)]) != 0:
                createNum(n, str(j))
        
        return res
