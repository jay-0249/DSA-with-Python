from collections import Counter
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        '''
        find a substring of s -> such that contain all characters & repititions of string t
        substring, slide over an iterable -> sliding window with variable size

        first make a hash map of frequency of characters in string t, using Counter data structure

        also initialise a counter variable representing the number of unique characters and repititions are still required
        
        intialise start and end(current) pointers for the sliding window

        slide over the string, for each iteration check if the character at the current pointer is required

        if freq of the current character is zero, decrement the counter

        if the counter is zero, update the length of the minimum substring and minimum substring

        while the counter is zero, decrement the start pointer and update the frequency and counter variable

        return the shortest substring of s such that it contains all characters and repititions of t
        '''
        #check for the edge case
        if len(s) < len(t):
            return ""

        #initialise start pointer of the window
        start = 0
        
        #initialise the frequency and counter variables
        freq_dict = Counter(t)
        counter = len(freq_dict)

        #initialise result variables for the worst case
        shortest_substring = str("")
        length_shortest_substring = len(s)+1

        for current in range(0,len(s)):
            #update freq_dict, counter based on the current character
            if s[current] in freq_dict:
                freq_dict[s[current]] -= 1
                if freq_dict[s[current]] == 0:
                    counter -= 1
            
            while counter == 0:
                #update the result if required based on current iteration
                length_current_substring = current-start+1
                if length_current_substring < length_shortest_substring:
                    length_shortest_substring = length_current_substring
                    shortest_substring = s[start:current+1]
                #update start pointer
                if s[start] in freq_dict:
                    if freq_dict[s[start]] == 0:
                        counter += 1
                    freq_dict[s[start]] += 1
                start += 1
                
        return shortest_substring
