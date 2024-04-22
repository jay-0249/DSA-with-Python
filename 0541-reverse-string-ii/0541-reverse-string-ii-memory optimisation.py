class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        """
        Iterate through the string, for the next 'k' characters, reverse the characters, then increment the index by 'k'
        continue to iterate this way until you are out of string index bounds
        """
        i = 0
        #we cannot mutate strings
        sList = [x for x in s]  
        while i < len(s):
            #reverse the string for 'k' characters
            left = i
            #Check for the last char possible to swap with the char at the left index
            if left+k > len(s):
                right = len(s)-1
            else:
                right = i + k - 1
            while left < right:
                sList[left], sList[right] = sList[right], sList[left]
                left += 1
                right -= 1
            #skip by 'k' charcters
            i += 2*k
        s = "".join(sList)
        return s