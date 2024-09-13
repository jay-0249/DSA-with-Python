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

        Approach 3: Using Array instead hashmap (dictionary)
        Create a array with all elements as 0 and index ranging from 0 to 25 as this question says characters that are used are 'a' to 'z' only
		Now iterate over the first string, at each iteration increase the count at the index equals ASCII difference of character and 'a'.
		Then iterate over the other array, at each iteration reduce the count if greater at 0, at the index equals ASCII difference of character and 'a', else return False
		Finally check if all elements in the array are zero.
		This can be done either by "iterating over the array and checking if each number is zero" or "simply checking if the count(0) equals the array length"
			
			Time Complexity : O(N) (Iterating over the arrays)
			Space Complexity: O(1) or O(K) as the number of unique characters possible is fixed 26 (a to z)
        """
        if len(s) != len(t):
            return False
        
        countChars = list(0 for i in range(0,26))

        for i in range(0, len(s)):
            charDiffS = ord(s[i])-ord('a')
            countChars[charDiffS] += 1

        for i in range(0, len(t)):
            charDiffT = ord(t[i])-ord('a')
            countChars[charDiffT] -= 1
        
        return len(countChars) == countChars.count(0)