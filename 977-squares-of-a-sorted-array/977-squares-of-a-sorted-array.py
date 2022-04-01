class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        na = []
        for n in nums:
            na.append(n**2)
            
        # n = len(nums)
        # for i in range(n-1):
        #     for j in range(0,n- i - 1):
        #         if na[j] > na[j + 1]:
        #             na[j], na[j + 1] = na[j + 1], na[j]
        # return na
        return sorted(na)
                
        