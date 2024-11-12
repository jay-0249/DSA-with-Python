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
        
        minElement = nums[0]
        l, r = 0, len(nums)-1
        while l<=r:
            mid = l + (r-l)//2
            print(l,r)
            if nums[mid] > minElement:
                l = mid+1
            else:
                minElement = nums[mid]
                r = mid-1
        print(l,r)
        minElement = min(nums[l], minElement, nums[r])
        
        return minElement
        
        