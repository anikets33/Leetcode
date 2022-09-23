class Solution:
    def concatenatedBinary(self, n: int) -> int:
        s = ''
        for i in range(1, n+1):
            s += bin(i)[2:]
            #print(s)
        n = int(s, 2)%1000000007
        return n
