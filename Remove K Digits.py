class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        if k == len(num):
            return '0'
        
        stack = [num[0]]
        i = 1
        while i<len(num):
            
            if k>0 and stack and stack[-1]>num[i]:
                stack.pop()
                k -= 1
            else:
                stack.append(num[i])
                i += 1
        
        while k>0:
            stack.pop()
            k -= 1
        
        res = ''.join(stack)
        return str(int(res))
