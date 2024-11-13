class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        '''
        Due to shifting the array with unknowun pivot index 'k', we will have original 0th to (k-1)th element shifted to last 'k' positions of the array 
        As we do not have any duplicate elements in the array, original 0th element will be at index len(nums)-k (where k is the index of the pivot element) such that 
        nums[len(nums)-k-1]>nums[len(nums)-k] and
        nums[len(nums)-k+1]>nums[len(nums)-k]
        Also let's use the fact that the original 0th term which is now nums[len(nums)-k] is less than the last
        '''
        pivot = 0   
        l, r = 0, len(nums)-1

        #If the sorted array is rotated, first element is greater than the last element
        #Then find the pivot element, and adjust left & right bounds to search target
        if nums[0] > nums[-1]:
            while l<r:
                mid = l+(r-l)//2
                if nums[mid]>nums[r]:
                    l = mid+1
                else:
                    r = mid
            pivot = l
            if target <= nums[-1]:
                l, r = pivot, len(nums)-1
            else:
                l, r = 0, pivot-1

        #Now search for target in between the left & right bounds
        while l<=r:
            mid = l+(r-l)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid-1
            else:
                l = mid+1
        return -1

