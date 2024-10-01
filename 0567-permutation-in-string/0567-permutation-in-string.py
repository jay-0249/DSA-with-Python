from collections import Counter

class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        '''
        if substring in s2 -> matches all chars & repititions of chars in s1 -> return true else false
        substring, iteration over iterable -> Sliding Window with fixed length

        use a frequency dictionary of s1, counter of unique characters required
        let's say k = len(s1)
        first check if the first k characters of s2 can be a permuatation of s1
        if count of unique character becomes zero, reduce the counter
        if counter becomes zero, return True

        else continue to slide over the string s2
        replace the character at start position of the window with character next to end psoition
        '''
        #check if s1 can be a substring of s2
        if len(s2) <len(s1):
            return False

        freq_dict = Counter(s1)
        counter = len(freq_dict.keys())
        #update frequency dictionary with first k-1 characters
        for current in range(len(s1)-1):
            if s2[current] in freq_dict:
                freq_dict[s2[current]] -= 1
                if freq_dict[s2[current]] == 0:
                    counter -= 1

        #iterating over the rest of the characters
        for current in range(len(s1)-1,len(s2)):
            #add the ending character
            if s2[current] in freq_dict:
                freq_dict[s2[current]] -= 1
                if freq_dict[s2[current]] == 0:
                    counter -= 1
            #check for the result variable
            if counter == 0:
                return True
            #remove the start character of the window
            start = current-len(s1)+1
            if s2[start] in freq_dict:
                if freq_dict[s2[start]] == 0:
                    counter += 1
                freq_dict[s2[start]] += 1
            
        return False
