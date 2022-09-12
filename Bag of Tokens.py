class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        
        tokens.sort()
        
        i, j = 0, len(tokens)-1
        score = 0
        m = 0
        
        while i<=j:
            if tokens[i] > power and score == 0:
                return 0
            if tokens[i] > power:
                power += tokens[j] 
                j -= 1
                score -= 1
            else:
                power -= tokens[i]
                i += 1
                score += 1
            m = max(score, m)
        
        return m
                
