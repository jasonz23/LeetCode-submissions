class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # num = 1
        # for n in nums:
        #     if num in nums:
        #         num +=1
        # return num O(n^2)
        num = 1
        nums.sort()
        for n in nums:
            if n == num:
                num +=1
        return num
        
        