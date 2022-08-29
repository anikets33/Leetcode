class Solution:
    def numTrees(self, n: int) -> int:
        
        mem = {0 : 1,
               1 : 1,
               2 : 2
              }            
            
        def count(n):
            if n in mem:
                return mem[n]
                
            s = 0
            for i in range(1, n+1):
                a = count(i-1) if i-1 not in mem else mem[i-1]
                b = count(n-i) if n-i not in mem else mem[n-i]
                mem[i-1] = a
                mem[n-i] = b
                
                s += (a*b)
            
            return s
                
        return count(n)
