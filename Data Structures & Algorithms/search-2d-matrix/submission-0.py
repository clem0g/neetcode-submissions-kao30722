class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if target == matrix[i][-1]:
                return True
            elif target > matrix[i][-1]:
                pass
            elif target < matrix[i][-1]:
                if target == matrix[i][0]:
                    return True
                elif target > matrix[i][0]:
                    l,r = 0, len(matrix[i])-1
                    while l <= r:
                        m = l + ((r - l)//2)
                        if matrix[i][m] > target:
                            r = m -1
                        elif matrix[i][m] < target:
                            l = m + 1
                        elif matrix[i][m] == target:
                            return True
        return False

