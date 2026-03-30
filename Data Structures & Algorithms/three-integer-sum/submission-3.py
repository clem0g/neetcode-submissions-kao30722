class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # Sort the array
        result = []
        
        for i in range(len(nums)):
            # 1. Skip duplicates for the fixed number 'i'
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            # 2. Set pointers. Left starts at i + 1 to avoid looking backward
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    # Found a triplet
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # 3. Skip duplicates for the 'left' pointer
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    # 4. Skip duplicates for the 'right' pointer
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                        
                    # 5. Continue searching for other pairs for this 'i'
                    left += 1
                    right -= 1
                    
        return result
                    
                    




        