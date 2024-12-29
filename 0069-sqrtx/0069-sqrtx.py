class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left, right = 0, x
        square_root = -1
        while left <= right:
            mid = left + (right-left)//2
            if mid*mid <= x:
                square_root = mid
                left = mid + 1
            elif mid*mid > x:
                right = mid - 1

        return square_root