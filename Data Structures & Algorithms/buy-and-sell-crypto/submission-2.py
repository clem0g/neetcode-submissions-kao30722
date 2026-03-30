class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minP = prices[0]
        maxP = 0

        for p in prices: 
            if p < minP:
                minP = p
            
            elif p - minP > maxP:
                maxP = p - minP
        return maxP

                    
