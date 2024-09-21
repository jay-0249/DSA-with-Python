class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        #create a set of all unique numbers in the array, so that we can check if a number exists in the array in O(1) time
        unique_numbers_set = set(nums)

        #initialise the length of the longest consecutive sequence to be 0
        max_length_consecutive_sequence = 0
        
        #Now iterate over the array to find the longest consecutive sequence possible 
        for i in nums:
            #Check if the current number in this iteration is the number to start a sequence
            if i-1 not in unique_numbers_set:
                length_consecutive_sequence = 1
                while i+1 in unique_numbers_set:
                    length_consecutive_sequence += 1
                    i += 1 
                if length_consecutive_sequence > max_length_consecutive_sequence:
                    max_length_consecutive_sequence = length_consecutive_sequence
        
        return max_length_consecutive_sequence