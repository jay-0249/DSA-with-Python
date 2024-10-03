class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        tempStack = []
        isValid = True

        def isValidClosingBracket(closedB):
            openB = tempStack.pop()
            if openB == '(' and closedB == ')':
                return True
            elif openB == '{'and closedB == '}':
                return True
            elif openB == '[' and closedB == ']':
                return True
            else:
                return False

        for b in s:
            if b=='(' or b=='{' or b=='[': #push opening brackets to stack
                tempStack.append(b)
            elif len(tempStack)==0: #if the stack is empty and we find a closing bracket
                isValid = False
                break
            elif not isValidClosingBracket(b):
                isValid = False
                break

        #Checking if we have any the opening brackets for those couln't found a matching bracket
        if len(tempStack) != 0:
            isValid = False

        return isValid  
        