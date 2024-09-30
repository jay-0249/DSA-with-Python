class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        '''
        Approach
        Use sliding approach as we have to find a substring, slide over the string
        Iterate over the string with start and current positions
        keep track of the repititions of the char that repeated most in the substring between start and current position
        If the difference between maximum repititions of a char that repeats most in the substring and the length of the substring, is greater than k, then decrement start by one.
        This is because, we can atmost replace k characters in a substring

        Time Complexity - O(N)
        Space Complexity - O(1)
        '''


        # count = {}
        
        # l = 0
        # maxf = 0
        # for r in range(len(s)):
        #     count[s[r]] = 1 + count.get(s[r], 0)
        #     maxf = max(maxf, count[s[r]])

        #     if (r - l + 1) - maxf > k:
        #         count[s[l]] -= 1
        #         l += 1

        # return (len(s) - l)


        #initialise start position
        start = 0

        #initialise iteration variable to keep track of frequency of the character that repeats most
        frequency_most_repeated_char = 0
        char_frequency_dictionary = dict()


        for current_position in range(len(s)):
            #update the frequency with the current character
            char_frequency_dictionary[s[current_position]] = 1 + char_frequency_dictionary.get(s[current_position],0)

            #update the frequency of the char most repeated
            frequency_most_repeated_char = max(frequency_most_repeated_char, char_frequency_dictionary[s[current_position]])

            #check if we need to replace more than k characters in this substring so that the substring contains same character
            if (current_position - start+1) - frequency_most_repeated_char > k:
                char_frequency_dictionary[s[start]] = char_frequency_dictionary[s[start]] - 1
                start += 1
            
        return len(s)-start