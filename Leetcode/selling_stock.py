prices = [2,4,1] 

profit = 0
buying_day = min(prices)

if buying_day in prices:
    index = prices.index(buying_day)
    days_for_selling = prices[index + 1:]

    selling_day = max(days_for_selling)

    profit = selling_day - buying_day

    print(profit)
else: 
    profit = 0 
    print(profit)
    

# 

class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0

        min_price = prices[0]  # Initialize the minimum price as the first price
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            else:
                max_profit = max(max_profit, price - min_price)

        return max_profit
