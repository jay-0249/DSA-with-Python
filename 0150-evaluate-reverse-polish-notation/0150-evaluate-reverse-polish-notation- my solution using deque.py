from collections import deque
import math
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        operationsDict = {"+","-","*","/"}
        stack = deque()

        for t in tokens:
            if t in operationsDict:
                secondOperand = stack.pop()
                firstOperand  = stack.pop()
                
                if t=="+":
                    result = firstOperand + secondOperand
                elif t=="-":
                    result = firstOperand - secondOperand
                elif t=="*":
                    result = firstOperand*secondOperand
                else:
                    result = int(round(firstOperand/secondOperand,0))
                    if result<0 and firstOperand != result*secondOperand:
                        result += 1
                stack.append(result)
            else:
                stack.append(int(t))

        return stack.pop()
        