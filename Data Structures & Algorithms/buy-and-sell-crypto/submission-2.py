class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==1:
            return 0
        l, r = 0, 1
        mx = 0
        while r < len(prices):
            buy, sell = prices[l], prices[r]
            if buy < sell:
                if mx < sell-buy:
                    mx = sell-buy
            else:
                l=r
            r += 1
        return mx