class Solution:
    def trap(self, height: List[int]) -> int:
        c = 0
        maxRight = height[-1]
        maxLeft = height[0]
        i = 1
        j = len(height) - 1
        while i<=j:
            q = 0
            #print(maxLeft, maxRight)
            if maxLeft < maxRight:
                q = maxLeft - height[i]
                maxLeft = max(maxLeft, height[i])
                i += 1
            else:
                q = maxRight - height[j]
                maxRight = max(maxRight, height[j])
                j -= 1
            c = c + q if q > 0 else c
        
        return c
