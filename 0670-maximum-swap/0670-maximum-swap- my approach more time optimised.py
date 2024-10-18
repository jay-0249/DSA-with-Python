class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num < 11:
            return num
        #unitdigit to highest digit
        digits = list(map(int,str(num)))
        
        #print(digits)
        #Find the last digit that can be replaced
        #In a number when we traverse from left to right(units digit), if the digits are in non-increasing sequence then we do not have to replace any of the digits, as the non-increasing pattern makes it the highest possible with those digits. Example 9973, 86332210
        #But while traversing from left to right, if we have increasing sequence at any digit then we it for sure, we can replace a digit from the left most digit to the current digit. Example 86342, 86349 which would become 86432, 96348
        #There if we have an instance of increasing sequence at any digit, we have to find the largest digit of the rest of the digits to the right part of that digit where increasing pattern is spotted. Now iterate in the left part to see where can we fit this highest digit of the right part.
        LastDigitCanBeReplacedIndex = len(digits)-1
        for i in range(0, len(digits)-1, 1):
            currDigit = digits[i]
            #print(i)
            nextDigit = digits[i+1]
            if currDigit < nextDigit:
                LastDigitCanBeReplacedIndex = i
                break
        #print(LastDigitCanBeReplacedIndex , "LastDigitCanBeReplacedIndex")
        #Find the highest digit in the right part of the number from the digit where first increasing pattern is spotted
        maxDigitIndexToReplace = LastDigitCanBeReplacedIndex
        for i in range(maxDigitIndexToReplace, len(digits), 1):
            if digits[i] >= digits[maxDigitIndexToReplace]:
                maxDigitIndexToReplace = i
        #Traverse from the leftmost digit to the digit where first increasing pattern is spotted. See where we can fit highest digit of the right part of the number from the digit where first increasing pattern is spotted
        for i in range(0,LastDigitCanBeReplacedIndex, 1):
            if digits[i] < digits[maxDigitIndexToReplace]:
                LastDigitCanBeReplacedIndex = i
                break
        #Replace the digits
        if not LastDigitCanBeReplacedIndex == maxDigitIndexToReplace:
            temp = digits[LastDigitCanBeReplacedIndex]
            digits[LastDigitCanBeReplacedIndex] = digits[maxDigitIndexToReplace]
            digits[maxDigitIndexToReplace] = temp

        #print(digits)
        result = int(''.join(map(str, digits)))
        return result


        