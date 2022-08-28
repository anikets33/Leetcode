class Solution:
    def removeStars(self, s: str) -> str:
        res = ''
        for each in s:
            if each == '*':
                res = res[:-1]
            else:
                res += each
        return res
