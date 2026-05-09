class Solution:
    def maxProfit(self, prices: List[int]) -> int:



        #want to iterate through the prices array with two pointers
        #until the right pointer reaches the end 
        #every time the right pointer value is greater than the value
        #at the left pointer you want to check the profit from prices on index
        # right - left. if bigger thats the new max
        #if they are the same value l and r or r is less than that is the new lowest day to buy stock
        

        l,r = 0, 1
        maxP = 0
        while r < len(prices):

            if prices[l] < prices[r]:
                profit = prices[r]-prices[l]
                maxP = max(maxP,profit)

            else:
                l = r

            r +=1

        return maxP
        