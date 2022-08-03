class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        l = list(sentence.split())
        n = len(l)
        for i in range(1, n+1):
            if l[i-1][0] in ['a', 'e', 'i', 'o', 'u', 'E', 'A', 'I', 'O', 'U']:
                l[i-1] = l[i-1] + 'ma' + 'a'*i
            else:
                #print(l[i-1])
                l[i-1] = l[i-1][1:] + l[i-1][0] + 'ma' + 'a'*i
        
        return ' '.join(l)
