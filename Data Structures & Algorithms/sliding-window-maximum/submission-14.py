class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
# The Deque will store INDICES, not values.
        # It will always be sorted by value: High -> Low
        q = deque() 
        res = []
        l = 0

        for r in range(len(nums)):
            # 1. Pop smaller values from the back
            # While the new number is bigger than the last number in queue...
            while q and nums[q[-1]] < nums[r]:
                q.pop() # Remove the "useless" small number

            # 2. Add our new number's index
            q.append(r)

            # 3. Remove old values from the front
            # If the index at the front is to the left of our window 'l'...
            if l > q[0]:
                q.popleft()

            # 4. Add to result (once window is full size)
            if (r + 1) >= k:
                # The max is ALWAYS at the front!
                res.append(nums[q[0]])
                l += 1
                
        return res



        