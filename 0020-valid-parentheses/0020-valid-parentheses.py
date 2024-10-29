class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        '''
        Using array to store open brackets and and a variable to track the length of the array.
        Iterate over the loop, if we find a closing bracket, check if the previous opening bracket is suitable for this closing bracket, if yes pop the opening bracket else it is a invalid string. This way we ensure "Every close bracket has a corresponding open bracket of the same type" and "Open brackets must be closed in the correct order"
        After iteration let's check if the array is empty or not. If yes, it is true that "Open brackets must be closed by the same type of brackets"

        Time Complexity: O(N)
            Traversing the array - O(N)
            Inserting or Deleting an elements from the array - O(1) on an average
            Inserting or Deleting atmost half of chars of s from the array- O(N) on an average
        
        Space Complexity: O(N)
            bracketDict - O(1)
            lengthArray - O(1)
            Inserting or Deleting an elements from the array - O(1)
            Inserting or Deleting atmost half of chars of s from the array- O(N)
        '''
        isValid = True
        bracketDict = {")":"(", "}":"{", "]":"["}
        bracketArray = []
        lengthArray = 0

        for b in s:
            if b in bracketDict:
                if bracketArray and lengthArray > 0:
                    if bracketDict[b] == bracketArray[lengthArray-1]:
                        bracketArray.pop()
                        lengthArray -= 1
                    else:
                        return False
                else:
                    return False
            else:
                bracketArray.append(b)
                lengthArray += 1

        if lengthArray == 0:
            return True
        else:
            return False