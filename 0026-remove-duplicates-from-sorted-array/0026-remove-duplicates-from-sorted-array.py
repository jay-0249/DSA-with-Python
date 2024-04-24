class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        Array is sorted and we have to swap/copy elements. Therefore, 2 pointer may be used.
        use two pointers,
        with 1st pointer 'prevUnique' indicating the prevUnique number found, starting at '0'
             2nd pointer 'i' indicating the current number starting at '1'
             iterate over the array, check if the number at 'i' i.e, current number is same as the previous unique number found, if it is iterate until you find another unique number in bounds, copy the next unique number found to the next index of previous unique number.
             if the current number is unique, copy it to the next index of previous unique number.
        Proceed until the current number's index is not out of bounds
        Return the unique number of numbers as prevUniqueNumIdx + 1
        Edgecase: array of length 0 or 1
        """
        if len(nums)<2:
            return len(nums)

        prevUniqueNumIdx, currentNumIdx = 0,1
        while currentNumIdx < len(nums):
            if nums[currentNumIdx] == nums[prevUniqueNumIdx]:
                #Iterate until you find next unique number
                """
                #we iterate to find next unqiue even if the following while loop is omitted
                while currentNumIdx < len(nums) and nums[currentNumIdx] == nums[prevUniqueNumIdx]:
                    currentNumIdx += 1
                """
                currentNumIdx += 1
            else:
                #Copy the next unique number to index next to previous unique number
                #We copy, as we have to return the array with all 'k' unique numbers arranged from index '0' to 'k-1'
                nums[prevUniqueNumIdx + 1] = nums[currentNumIdx]
                prevUniqueNumIdx += 1
                currentNumIdx += 1
                
        return prevUniqueNumIdx + 1
