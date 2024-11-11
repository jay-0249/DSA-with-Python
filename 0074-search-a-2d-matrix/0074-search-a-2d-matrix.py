class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m, n = len(matrix), len(matrix[0])
        l, r = 0, m*n-1
        while l<=r:
            mid = l+(r-l)//2
            midM= (mid)//n
            midN = (mid)%n
            if matrix[midM][midN] == target:
                return True
            elif matrix[midM][midN] > target:
                r = mid-1
            else:
                l = mid+1
        return False

