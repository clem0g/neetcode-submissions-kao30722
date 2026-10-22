class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = 0
        
        for i in range(len(nums)):
            left = i
            right = left + 1
            while right < len(nums):
                if(nums[left] + nums[right]) == target:
                    return [left,right]
                else:
                    right +=1
                    