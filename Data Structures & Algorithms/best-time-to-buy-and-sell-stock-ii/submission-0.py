class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prices.append(0)
        sell=prices[0]
        profit = 0
        for i in range(1,len(prices)):
            if prices[i]<prices[i-1]:
                profit+=prices[i-1]-sell
                sell=prices[i]
        return profit 