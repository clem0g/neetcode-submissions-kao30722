class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        l, r = 0, len(height) - 1
        left_max, right_max = 0, 0
        water = 0
        
        while l < r:
            # Check which side is the bottleneck (the shorter wall)
            if height[l] < height[r]:
                # If current bar is taller than previous max, update max
                # Otherwise, it traps water!
                if height[l] >= left_max:
                    left_max = height[l]
                else:
                    water += left_max - height[l]
                l += 1
            else:
                # Same logic for the right side
                if height[r] >= right_max:
                    right_max = height[r]
                else:
                    water += right_max - height[r]
                r -= 1
                
        return water

        



