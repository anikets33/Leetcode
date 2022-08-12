class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        c = 0
        d = {}
        
        for i in range(len(time)):
            time[i] %= 60
            
        for each in time:
            target = 60-each
            if each == 0 and 0 in d:
                c += d[0]
            elif target in d:
                c += d[target]
            if each in d:
                d[each] += 1
            else:
                d[each] = 1
        
        return c
        
        
        
