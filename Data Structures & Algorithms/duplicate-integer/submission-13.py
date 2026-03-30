class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        space = []
        for i in nums:
            if i in space:
                return True
            else:
                space.append(i)
        return False
                