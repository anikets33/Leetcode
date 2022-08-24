class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n > 0:
            a = math.log10(n)/math.log10(3)
            if a%1 == 0:
                return True
        return False
