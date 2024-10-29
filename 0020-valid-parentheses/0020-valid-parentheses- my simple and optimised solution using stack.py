from collections import deque

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        '''
        Using stack to store open brackets.
        Iterate over the loop, if we find a closing bracket, check if the previous opening bracket is suitable for this closing bracket, else it is a invalid string. This way we ensure "Every close bracket has a corresponding open bracket of the same type" and "Open brackets must be closed in the correct order"
        After iteration let's check if the stack is empty or not. If yes, it is true that "Open brackets must be closed by the same type of brackets"

        Time Complexity: O(N)
            Traversing the array - O(N)
            Inserting or Deleting an elements from the stack - O(1) on an average
            Inserting or Deleting atmost half of chars of s from the stack - O(N) on an average
        
        Space Complexity: O(N)
            bracketDict - O(1)
            Inserting or Deleting an elements from the stack - O(1)
            Inserting or Deleting atmost half of chars of s from the stack - O(N)
        '''
        isValid = True
        bracketDict = {")":"(", "}":"{", "]":"["}
        bracketStack = deque()

        for b in s:
            if b in bracketDict:
                if bracketStack:
                    lastOpeningBracket = bracketStack.pop()
                else:
                    return False
                if bracketDict[b] != lastOpeningBracket:
                    return False
            else:
                bracketStack.append(b)

        if len(bracketStack) == 0:
            return True
        else:
            return False