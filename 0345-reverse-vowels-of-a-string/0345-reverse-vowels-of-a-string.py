class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        """
        Reverse the vowels only by swaping characters
        Iterate from the start until you find a vowel. Similarly iterate from the end until you find a vowel.
        Then swap the vowels at start and end pointers
        Proceed to iterate this way until start<end
        This approach is optimise to remove Boolean check flags. Also use 'set' for vowels for comparing which further reduces the time O(5) to O(1) and the need to lowercase the character at each comparision  
        """
        start, end = 0, len(s)-1
        vowels = set('aeiouAEIOU')
        #Convert string into list as 'unicode' object - string is immutable
        #Fun fact: Tuple is not a unicode object but is immutable in python
        #list(s) or s.split(), slist = [x for a,x in enumerate(s)]
        sList = [x for x in s]
        while start < end:
            while start < end and sList[start] not in vowels:
                start += 1
            while start < end and sList[end] not in vowels:
                end -= 1
            if start < end:
                temp = sList[start]
                sList[start] = sList[end]
                sList[end] = temp
                start += 1
                end -= 1
                
        return ''.join(sList)