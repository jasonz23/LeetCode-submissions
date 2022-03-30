class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i1, n in enumerate(matrix):
            for m in n:
                if m == target:
                    return True
        return False
        