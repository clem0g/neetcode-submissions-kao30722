class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        prev = {}
        for i in range(len(nums)):
            prev[nums[i]] = 1 + prev.get(nums[i],0)
            if prev[nums[i]] >= 2:
                return nums[i]
        


