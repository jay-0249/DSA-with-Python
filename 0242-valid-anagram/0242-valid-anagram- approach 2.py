class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        """
        A anagram is a string formed by rearranging the characters of the string using all original characters exactly once
        To check if a string is anagram of other, the unqiue characters and the number of times they occur/repeat in a string should be same in both strings

        Approach 2: A LITTLE MORE OPTIMISED IN TIME AND SPACE COMPLEXITY
        Anagrams cannot be of different lengths as per the definition, so check if the both the strings are of same length
        Then proceed to create a hashmap (dictionary) with the unique characters and their number of occurance in the string for a string.
        Then iterate over the other array, in each iteration reduce the count of the element in the dictionary, after each iteration check if the count of element in the dictionary is zero, if it is zero delete that key from the dictionary
        Finally, after iterating over the other string, the dictionary should be empty if both these strings are anagram of each other. So the length of the dictionary now should be zero.

        Time Complexity: O(N) (As the dictionary creation is an iteration over the array)
        Space Complexity: O(1) or O(K) where K is the number of characters or alphabets possible which is a fixed number
        """
        if len(s) != len(t):
            return False
        
        dictStrS = {}

        for i in s:
            dictStrS[i] = 1+dictStrS.get(i,0)
        
        for i in t:
            if i in dictStrS:
                dictStrS[i] = dictStrS.get(i)-1
            else:
                return False
            if dictStrS[i] == 0:
                del dictStrS[i]
        
        return len(dictStrS) == 0
