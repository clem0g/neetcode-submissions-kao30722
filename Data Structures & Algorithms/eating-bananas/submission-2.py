import math

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        # The answer must be between 1 and the maximum pile size
        left, right = 1, max(piles)
        res = right # Default to the max possible speed
        
        while left <= right:
            k = (left + right) // 2
            
            # Calculate total hours needed to eat all bananas at speed k
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)
                
            # If Koko can finish within h hours, try to find a slower speed
            if hours <= h:
                res = min(res, k)
                right = k - 1
            # If it takes too long, she must eat faster
            else:
                left = k + 1
                
        return res


