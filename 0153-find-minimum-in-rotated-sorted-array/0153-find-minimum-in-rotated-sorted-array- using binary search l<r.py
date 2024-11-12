class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        If a sorted array is rotated if all elements are unique, 
            a[n-1] < a[0] < a[1]
        else the array is not rotated
        
        Brute force would be iterating linearly from the first element.

        '''
        if nums[0] <= nums[-1]:
            return nums[0]
        

        l, r = 0, len(nums)-1
        
        while l<r:
            mid = l + (r-l)//2

            if nums[mid] > nums[r]:
                l = mid+1
            else:
                r = mid
 

        return nums[l]
        
        