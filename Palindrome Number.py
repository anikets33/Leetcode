class Solution:
    def isPalindrome(self, x: int) -> bool:
        i = reverse = 0
        n = x

        while n>0:
            
            reverse = (n%10) + reverse*10
            i += 1
            n = n//10
        
        return reverse == x
