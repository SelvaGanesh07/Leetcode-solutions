class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        d=prices[0]
        p=0
        for i in range(1,len(prices)):
            if prices[i]<d:
                d=prices[i]
            if prices[i]-d>p:
                p=prices[i]-d
        return p