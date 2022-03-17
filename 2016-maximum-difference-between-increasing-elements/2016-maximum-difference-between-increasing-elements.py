class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        i = 0
        diff = 0
        while i < len(nums):
            j = i+1
            while j < len(nums):
                if nums[j] - nums[i] > diff:
                    diff = nums[j] - nums[i]
                j += 1
            i += 1
        if diff == 0:
            return -1
        else:
            return diff
            
        