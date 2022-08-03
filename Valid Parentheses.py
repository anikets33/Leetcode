class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        
        for each in s:
            if each in ['(', '{', '[']:
                stack.append(each)
            else:
                if stack:
                    if (stack[-1] == '(' and each == ')') or (stack[-1] == '{' and each == '}') or (stack[-1] == '[' and each == ']'):
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        
        if stack:
            return False
        else:
            return True
