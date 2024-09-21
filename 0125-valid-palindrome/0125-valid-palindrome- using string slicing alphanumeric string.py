class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        #convert the string into lowercase alphanumeric string
        alpha_numeric_string = ""
        for i in s:
            if i.isalnum():
                alpha_numeric_string += i.lower()
        
        #verify if the alphanumeric string is a palindrome using string slicing
        return alpha_numeric_string == alpha_numeric_string[::-1]

        