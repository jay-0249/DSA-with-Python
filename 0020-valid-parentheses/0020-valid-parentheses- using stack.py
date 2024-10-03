class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        '''
        Using stack to check if a parenthesis order is correct. Stack follows LIFO (Last In First Out) which resembles the parenthesis order matching procedure.

        Use dictionary to store 
        '''
        temp_stack = []
        is_valid = True

        matching_dictionary = { "(":")","{":"}","[":"]"}

        for i in s:
            if i in matching_dictionary:
                temp_stack.append(i)
            elif len(temp_stack)>0 and matching_dictionary[temp_stack[-1]] == i:
                temp_stack.pop()
            else:
                is_valid = False
                return is_valid
        
        if len(temp_stack) == 0:
            is_valid = True
        else:
            is_valid = False

        return is_valid
        