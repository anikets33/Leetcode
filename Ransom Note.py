class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d = Counter(magazine)
        
        for each in ransomNote:
            if each in d and d[each]>0:
                d[each] -= 1
            else:
                return False
        return True
