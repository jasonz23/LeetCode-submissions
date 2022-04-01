class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        na = []
        for n in nums:
            na.append(n**2)
            
        return sorted(na)
        