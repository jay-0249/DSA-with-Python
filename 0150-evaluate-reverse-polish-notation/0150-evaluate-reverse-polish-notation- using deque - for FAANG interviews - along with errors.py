from collections import deque

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
                    if secondOperand == 0:
                        raise ZeroDivisionError("Cannot perform divison with zero")
                    result = int(firstOperand/secondOperand)
                    if result<0 and firstOperand % secondOperand != 0:
                        result += 1

                stack.append(result)
            else:
                try:
                    stack.append(int(t))
                except ValueError:
                    raise TypeError("Please enter an integer or a valid arithmetic operator")

        if len(stack) != 1:            
            raise ValueError("Invalid Reverse Polish Notation expression")
        
        return stack.pop()

        