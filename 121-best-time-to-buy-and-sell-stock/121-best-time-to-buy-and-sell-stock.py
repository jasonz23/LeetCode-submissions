class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyPrice = prices[0] 
        maxProfit = 0 
        for i in range(1,len(prices)):
            if prices[i] < buyPrice: 
                buyPrice = prices[i] 
            else:  # else
                maxProfit = max(maxProfit, prices[i] - buyPrice)
        return maxProfit  #answer
            
        