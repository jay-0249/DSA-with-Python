class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0, len(nums)-1
        while l<=r:
            mid = l+(r-l)//2
            #Compare the target with the number at index 'mid'
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                r = mid - 1
            # nums[mid] < target < nums[mid+1] that target is not present in the array and so if we have to insert 'target' in the array, we have to insert it at the index 'mid+1'
            elif mid+1 < len(nums) and target < nums[mid+1]:
                return mid+1
            else:
                l = mid+1
        
        if target > nums[len(nums)-1]:
            return len(nums)
        else:
            return 0