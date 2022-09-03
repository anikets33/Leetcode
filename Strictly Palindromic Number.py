class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        
        def create(n, i):
            s = ''
            while n>0:
                s = str(n%i) + s
                n = n//i
            return s
        
        def isPalin(s):
            return s == s[::-1]
        
        for i in range(2, n-1):
            s = create(n, i)
            if not isPalin(s):
                return False
        return True
