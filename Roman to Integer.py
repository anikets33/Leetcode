class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1
        }
        num = 0
        prev = 5000
        for each in s:
            if roman[each] > prev:
                num -= 2*prev
            num += roman[each]
            prev = roman[each]
        return num
