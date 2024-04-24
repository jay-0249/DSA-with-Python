class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Edgecase - array of length - 0 or 1
        if len(nums)<2:
            return len(nums)
        #First unique number we visit is at index '0'
        prevUniqueNumIdx = 0
        #Let's start finding other unique number or their second copies
        secondCopyNotFound = True
        currentNumIdx = 1
        while currentNumIdx < len(nums):
            #If the current number is not same as the previous unique number we found or the current number is the second copy of the previous unique number
            if nums[currentNumIdx] != nums[prevUniqueNumIdx] or secondCopyNotFound:
                if nums[currentNumIdx] != nums[prevUniqueNumIdx]:
                    secondCopyNotFound = True
                else:
                    secondCopyNotFound = False
                nums[prevUniqueNumIdx + 1] = nums[currentNumIdx]
                prevUniqueNumIdx += 1
            #Iterate to next number in the array
            currentNumIdx += 1

        return prevUniqueNumIdx+1