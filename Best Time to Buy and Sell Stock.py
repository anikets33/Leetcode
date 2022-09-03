class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = prices[0]
        maxi = -math.inf
        
        for i in range(1, len(prices)):
            if prices[i] <= mini:
                mini = prices[i]
            else:
                maxi = max(maxi, prices[i] - mini)
        
        return max(0, maxi)
