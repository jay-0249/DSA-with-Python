class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        #Sliding Window, the profit for each adjacent days may summed to get window profit. Calculate max of such window profits
        #create an array of adjacent day profits

        adj_profit = []

        for i in range(0, len(prices)-1):
            adj_profit.append(prices[i+1] - prices[i])

        left = 0
        profit = 0
        max_profit = 0

        for right in range(0, len(adj_profit)):
            while profit < 0:
                profit -= adj_profit[left]
                left += 1

            profit += adj_profit[right]
            max_profit = max( max_profit, profit)
            
        
        return max_profit