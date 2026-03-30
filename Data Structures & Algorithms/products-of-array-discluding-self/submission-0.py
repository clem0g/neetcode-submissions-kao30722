class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            if nums[i] == 0:
                nums.pop(i)
                result = math.prod(nums)
                total = int(result/ 1)
                nums.insert(i, 0)
                output.append(total)
            else:
                result = math.prod(nums)
                total = int(result/ nums[i])
                output.append(total)
        return output


