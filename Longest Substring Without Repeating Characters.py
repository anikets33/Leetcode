class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        storage = {}
        i = longest = start = 0
        
        while i<len(s):
            if s[i] in storage:
                index = storage[s[i]]
                longest = max(longest, i-start)
                start = index + 1
            storage[s[i]] = i
            i += 1
            
        longest = max(longest, i-start)
        
        return longest
                
