# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 1, n
        while l<=r:
            mid = l+(r-l)/2
            if isBadVersion(mid):
                if mid>0 and isBadVersion(mid-1):
                    r = mid-1
                else:
                    return mid
            else:    
                l = mid+1

        return 1
