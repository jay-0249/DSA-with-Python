class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        
        def generateValidBracket(combination, openBracketsUsed):
            #Return if we have valid combination
            if len(combination) == 2*n:
                if openBracketsUsed == n:
                    result.append(combination)
                return
            #If we can insert more open brackets
            if openBracketsUsed < n:
                generateValidBracket(combination+"(", openBracketsUsed+1)
            #If we can insert more closed brackets
            #openBracketsUsed - closedBracketsUsed
            if (openBracketsUsed) - (len(combination) - openBracketsUsed) > 0:
                generateValidBracket(combination+")", openBracketsUsed)

        generateValidBracket("",0)
        
        return result

        