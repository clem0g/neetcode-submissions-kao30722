class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num = set(nums)
        longest_streak = 0
        current_num = 0

        for i in num:
            if i - 1 not in num:
                current_num = i
                current_streak = 1
                while current_num + 1 in num:
                    current_streak += 1
                    current_num += 1
                longest_streak = max(longest_streak, current_streak)
            if i - 1 in num:
                continue
        return longest_streak 





        