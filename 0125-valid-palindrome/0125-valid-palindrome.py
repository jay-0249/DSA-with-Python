class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        '''Iterating over to check if it is a palindrome'''
        i = 0
        j = len(s)-1
        while i<j:
            if not s[i].isalnum():
                i+=1
            elif not s[j].isalnum():
                j-=1
            elif s[i].lower() == s[j].lower():
                i += 1
                j -= 1
            else:
                return False
        
        '''If it is not a palindrome, it will be caught in the 'else' condition. Therefore the string is a palindrome, iteration will be succesful without getting caught with the 'else' '''
        return True
        