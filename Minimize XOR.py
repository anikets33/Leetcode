class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        a = bin(num1)[2:]
        c = bin(num2)[2:].count('1')
        s = ''
                
        for each in a:
            if c>0 and each == '1':
                c -= 1
                s += '1'
            else:
                s += '0'
        
        i = len(s)-1
        while i>=0:
            if c>0 and s[i] == '0':
                s = s[:i] + '1' + s[i+1:]
                c -= 1
            i -= 1
            
        if c>0:
            s = s + '1'*c
        
        return int(s,2)
