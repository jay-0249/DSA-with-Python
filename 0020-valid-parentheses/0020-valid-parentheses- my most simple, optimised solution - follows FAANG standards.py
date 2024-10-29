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
            Inserting or Deleting atmost half of chars of s from the stack - O(N)
        
        Space Complexity: O(N)
            bracketDict - O(1)
            Inserting or Deleting atmost half of chars of s from the stack - O(N)
        
        NOTE:
        Though the approach using array and stack have same order of time and space complexity, the solution using stack implemented using deque was faster and required lesser space.
        Because, deque is optimised for poping and appending element with O(1) order of Time & Space complexity 
        '''
        
        #dictionary to map closing and opening brackets
        bracketDict = {")":"(", "}":"{", "]":"["}
        bracketStack = deque()

        for b in s:
            if b in bracketDict:
                #return false when either the stack is empty or last opening bracket is not suitable closing bracket
                if not bracketStack or bracketStack.pop() != bracketDict[b]:
                    return False
            else:
                bracketStack.append(b)

        #return True if the stack is empty, meaning all brackets are valid
        return not bracketStack