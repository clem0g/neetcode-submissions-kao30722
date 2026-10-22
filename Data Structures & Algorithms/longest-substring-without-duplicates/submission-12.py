class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        max_s = 0
        prev = 0

        if (len(s) == 0):
            return 0 
        if (len(s) == 1):
            return 1

        for i in range(len(s)):
            chars.add(s[i])
            if len(chars) > max_s: 
                max_s = len(chars)
            if len(chars) == prev:
                chars.clear()
                chars.add(s[i])
            prev = len(chars)
        return max_s








