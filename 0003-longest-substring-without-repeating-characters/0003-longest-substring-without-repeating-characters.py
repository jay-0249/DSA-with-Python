class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        #initialise start position the end position is covered by using a for loop
        start = 0

        #intialise a set to keep track of the unique elements set in the substring between start and current position
        unique_elements_set = set ()

        #initialise the result length of the longest substring
        length_longest_string = 0

        #iterate over the string
        for current_position in range(0,len(s)):
            #char repeat scenario: if the current character is already in the string, move start position until next to such character
            while s[current_position] in unique_elements_set:
                unique_elements_set.remove(s[start])
                start += 1
            
            #add the current character to the unique elements set
            unique_elements_set.add(s[current_position])

            #update the result
            length_longest_string = max(length_longest_string, 1+current_position-start)

        #return the result
        return length_longest_string