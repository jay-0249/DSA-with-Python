class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        '''
        find longest substring
        sliding window with variable length
        start, current pointers
        as len(s) = 1,
        in the worst case answer, the longest substring can be of length 1
        similarly freq_max_repeated_char can be 1 in the worst case
        At each point, we see the frequency of the current character, increment the character count, if it is greater than maximum frequency, we will update the maximum frequency
        If length - maximum frequency is greater than k, then we have a case where we might need more than k replacements
        so increment the start pointer, decrement the start element frequency
        this way our substring is always in compliance with the maximum k repititions rule
        we do not need to worry about the freq_max_repeated_char, as if we find a case when we have a greater frequency, we will update freq_max_repeated_char
        also in each iteration we will check if we have found a longer string and update accordingly
        '''

        length_longest_string = 0
        start = 0

        freq_max_repeated_char = 0
        freq_dict = {}

        for current in range(0,len(s)):
            freq_dict[s[current]] = 1 + freq_dict.get(s[current], 0)
            freq_max_repeated_char = max(freq_max_repeated_char, freq_dict[s[current]])

            if ((current-start+1) - freq_max_repeated_char) > k:
                freq_dict[s[start]] -= 1
                start += 1

            length_longest_substring = max(current-start+1, length_longest_string)
        
        return length_longest_substring
