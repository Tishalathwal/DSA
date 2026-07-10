class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = prices[0]
        max_price = 0

        i =1

        while i<len(prices):
            if prices[i]<min_price:
                min_price = prices[i]

            else:
                profit = prices[i]- min_price
                
                if profit > max_price:
                    max_price = profit

            i += 1
        return max_price