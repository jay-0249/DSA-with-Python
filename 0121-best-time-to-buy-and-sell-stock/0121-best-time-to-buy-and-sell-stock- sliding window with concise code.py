class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        #initialise the result variable
        #As we do not want loss, so the worst case would be buying and selling the stock on the same day which is zero profit
        max_profit = 0
        
        lowest_price = prices[0]

        for current_price in prices:
            #loss scenario
            if current_price < lowest_price:
                lowest_price = current_price
            #profit scenario or no profit scenario
            else:
                #update max_profit scenario
                max_profit = max(max_profit, current_price-lowest_price)

        return max_profit