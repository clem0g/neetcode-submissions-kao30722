class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # total = len(nums1) + len(nums2)
        # if total % 2 == 0:
        #     middle1 = total//2
        #     middle2 = middle1 + 1
        # else:
        #     middle = total //2
        # median = (nums1[0]+nums2[-1])/2
        # return median

        num = nums1 + nums2
        num = sorted(num)
        if len(num) % 2 == 0:
            middle1 = len(num)//2
            middle2 = middle1 - 1
            median = (num[middle1] + num[middle2])/2
        else:
            middle = len(num)//2
            median = num[middle]
        return median
        # median = (max(num) + min(num))/2
        # return median