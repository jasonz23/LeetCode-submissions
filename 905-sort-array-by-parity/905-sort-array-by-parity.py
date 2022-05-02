class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        list1 = []
        list2 = []
        for n in nums:
            if n % 2 == 0:
                list1.append(n)
            else:
                list2.append(n)
        return list1 + list2
                             
                
        