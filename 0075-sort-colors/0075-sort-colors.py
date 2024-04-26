class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        """
        We will sort the colors using inplace swapping.
        let's have a index pointers for indicating the index last time we have stored '0' and '2'
        We will iterate over the array, at the current idex if we have '2' we will swap it before the last '2' was copied, similary for '0' swap next to '0' was copied
        After swapping 2, we have to check if we swapped
        """
        if len(nums)<2:
            return len(nums)
            
        lastZeroIdxPointer = -1
        lastTwoIdxPointer = len(nums)
        currentIdxPointer = 0

        while currentIdxPointer < len(nums):
            if nums[currentIdxPointer] is 0:
                lastZeroIdxPointer += 1
            elif nums[currentIdxPointer] is 2:
                lastTwoIdxPointer -= 1
            currentIdxPointer += 1

        currentIdxPointer = 0
        while currentIdxPointer < lastZeroIdxPointer+1:
            nums[currentIdxPointer] = 0
            currentIdxPointer += 1
        while currentIdxPointer < lastTwoIdxPointer:
            nums[currentIdxPointer] = 1
            currentIdxPointer += 1
        while currentIdxPointer < len(nums):
            nums[currentIdxPointer] = 2
            currentIdxPointer += 1

        return nums