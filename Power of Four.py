class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        i = 0
        c = 0
        while n!=0:
            r = n&1
            n = n>>1
            if i%2 != 0 and r == 1:
                return False
            else:
                if c == 1 and r == 1:
                    return False
                if c == 0 and r == 1:
                    c = 1
            i += 1
        return True if c == 1 else False
# return n > 0 and n & (n-1) == 0 and len(bin(n)) % 2 == 1
