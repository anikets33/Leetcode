class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        f = set()
        m = min(a, b)
        for i in range(1, m+1):
            if a%i == 0 and b%i == 0:
                f.add(i)
        return len(f)
