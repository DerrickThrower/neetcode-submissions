class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        maxProf = 0

        l,r = 0,1

        while r < len(prices):

            if prices[l] < prices[r]:# if the right val is greater than the left
                cur = prices[r] - prices[l]
                maxProf = max(cur,maxProf)

            else:
                l = r #the right one is either smaller or equal we should move

            r +=1
        
        return maxProf
        