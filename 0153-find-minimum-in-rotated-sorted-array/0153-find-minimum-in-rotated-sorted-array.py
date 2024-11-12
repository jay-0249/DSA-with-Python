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
        
        Brute force would be iterating linearly from the first element until 

        '''
        minElement = (len(nums)-1, nums[-1])

        for i,val in enumerate(nums):
            if val < minElement[1]:
                minElement = (i,val)
        
        return minElement[1]
        