class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        s = list(words[0])
        
        for each in words:
            l = list(each)
            n = len(s)
            i = 0
            for _ in range(n):
                if s[i] not in l:
                    #print(s[i], s)
                    s.remove(s[i])
                else:
                    l.remove(s[i])
                    i += 1
                if len(s) == 0:
                    break
        return s
