class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==0 or len(prices)==1:return 0
        l=0
        r=1

        profit = prices[r] - prices[l]
        while l<r:
            if profit<0:
                l+=1
                profit=0
                if r<len(prices)-1:
                    r+=1
            else:
                profit = max(profit,prices[r] - prices[l])
                if r<len(prices)-1:
                    r+=1
                else:
                    l+=1
        return profit