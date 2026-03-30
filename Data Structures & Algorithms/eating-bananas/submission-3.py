import math

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        l,r = 1,max(piles)
        res = max(piles)
        while l<=r:
            k = l + ((r - l)//2)
            t = 0
            for i in piles:
                t += math.ceil(i/k) 
            if t <= h:
                res = min(res,k)
                r = k - 1
            else:
                l = k + 1
        return res



