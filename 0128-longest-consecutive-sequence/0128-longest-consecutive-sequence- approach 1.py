class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        keyword - find the longest consecutive sequence
        for a number, if we have to find if it is part of a sequence, we need to know if either number-1 or number+1 is also present in the array
        so lets iterate over the array to create a set of unique numbers
        now iterate over the array, in each iteration let's check if there exists a sequence for this number. lets's check if there exists a number-1 for a given number in this set, if there exists then it is clear that this number is not the starting number of the sequence, so proceed for next iteration
        else if we can't find number-1 in the set of unique numbers of the array, the number in this iteration is the least number of the sequence, so find the length of the sequence that is possible with this number being the least number of that sequence
        similarly complete iterating through the array to find the maximum length of such a sequence
        '''
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