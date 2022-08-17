class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        count = 0
        d = {}
        
        for each in words:
            s = ''
            for ch in each:
                s += morse[ord(ch) - 97]
            if s not in d:
                d[s] = 1
                count += 1
        
        return count
