class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        num = nums[0]
        li = nums[1:]
        for n in li:
            if num == n:

                return True
            else:
                num = n
        return False
        