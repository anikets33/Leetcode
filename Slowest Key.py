class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        c = keysPressed[0]
        m = releaseTimes[0]
        
        for i in range(1, len(keysPressed)):
            if releaseTimes[i] - releaseTimes[i-1] == m:
                if c < keysPressed[i]:
                    c = keysPressed[i]
            elif releaseTimes[i] - releaseTimes[i-1] > m:
                c = keysPressed[i]
                m = releaseTimes[i] - releaseTimes[i-1]
                    
        return c
