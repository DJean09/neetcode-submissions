class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # set max profit
        maxP = 0

        # set minimum buy to the first element
        minBuy = prices[0]

        # loop through each price
        for sell in prices:
            # set max profit to whichever is bigger
            maxP = max(maxP, sell - minBuy)
            # set minimum buy to whichever is smaller
            minBuy = min(minBuy, sell)
        
        return maxP