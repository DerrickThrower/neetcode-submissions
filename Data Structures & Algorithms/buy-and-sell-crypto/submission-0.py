class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = float('inf')
        max_profit = 0;

        for price in prices:#iterate through array

            minprice = min(minprice,price)# takes the minimum between 
            #the minimum price and the current price

            profit = price - minprice # calculates the profit if the minimum price is subtracted from the current price

            max_profit = max(max_profit, profit) #the max profit is checked if it has changed 


        return max_profit



        