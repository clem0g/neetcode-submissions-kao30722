class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        max_s = 0
        prev = 0

        for i in range(len(s)):
            chars.add(s[i])
            if len(chars) == prev:
                if len(chars) > max_s: 
                    max_s = len(chars)
                chars.clear()
                chars.add(s[i])
            prev = len(chars)
        return max_s








