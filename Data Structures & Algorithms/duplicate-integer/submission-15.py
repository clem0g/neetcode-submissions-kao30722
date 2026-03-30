class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        space = set()
        for i in nums:
            if i in space:
                return True
            else:
                space.add(i)
        return False
                