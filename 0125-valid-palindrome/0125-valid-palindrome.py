class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        '''
        Iterate over the string from both ends to see if the characters at left and right index are alphanumeric and if they are alphanumeric, then check if they match else return false
        '''
        s = s.lower()
        left_pointer = 0
        right_pointer = len(s) - 1

        while left_pointer < right_pointer:
            if s[left_pointer].isalnum() and s[right_pointer].isalnum() and s[left_pointer] != s[right_pointer]:
                print (left_pointer, right_pointer)
                return False
            elif not s[left_pointer].isalnum():
                left_pointer += 1
            elif not s[right_pointer].isalnum():
                right_pointer -= 1
            else:
                left_pointer += 1
                right_pointer -= 1

        return True
        