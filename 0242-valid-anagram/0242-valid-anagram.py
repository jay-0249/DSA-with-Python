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

        Approach 1:
        Anagrams cannot be of different lengths as per the definition, so check if the both the strings are of same length
        Then proceed to create a hashmap (dictionary) with the unique characters and their number of occurance in the string for both strings.
        Finally compare to see if the dictionaries are same.

        Time Complexity: O(N) (As the dictionary creation is an iteration over the array and also comparing dictionaries is again a iteration over the dictionary)
        Space Complexity: O(1) or O(K) where K is the number of characters or alphabets possible which is a fixed number
        """
        if len(s) != len(t):
            return False
        
        dictStrS, dictStrT = {}, {}

        for i in range(0, len(s)):
            dictStrS[s[i]] = 1+dictStrS.get(s[i],0)
            dictStrT[t[i]] = 1+dictStrT.get(t[i],0)
        
        return dictStrS == dictStrT
        
