
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l = 0
        max_len = 0
        
        for r in range(len(s)):
            # If the character is already in the window, 
            # shrink the window from the left until it's gone.
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            
            # Add the current character and update max length
            seen.add(s[r])
            max_len = max(max_len, r - l + 1)
            
        return max_len


        