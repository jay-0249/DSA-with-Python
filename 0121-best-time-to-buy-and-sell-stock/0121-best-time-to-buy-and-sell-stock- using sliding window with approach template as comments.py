class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        max_profit = 0
        start, end = 0, 0

        while end < len(prices):
            profit = prices[end]-prices[start]

            end += 1

            if max_profit < profit:
                max_profit = profit
            
            if profit<=0:
                start = end - 1

        return max_profit
        