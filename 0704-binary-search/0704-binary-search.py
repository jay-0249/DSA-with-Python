class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        '''
        The list is sorted. So rather than searching linearly we can search the ends and the middle element and narrow down similarly. This reduces our time to find the element from O(N) to O(logN)
        Time Complexity - O(logN)
        Space Complexity - O(1)
        '''
        l,r = 0, len(nums)-1

        while l<=r:
            mid = l+(r-l)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return -1
