class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """

        operators = {"+","-","*","/"}
        stack = []
        for i, token in enumerate(tokens):
            if token in operators:
                if len(stack)<2:
                    break
                op2 = stack.pop()
                op1 = stack.pop()
                if token == "+":
                    stack.append(op1+op2)
                elif token == "-":
                    stack.append(op1-op2)
                elif token == "*":
                    stack.append(op1*op2)
                else:
                    quotient = math.trunc(float(op1)/op2)
                    stack.append(quotient)
            else:
                stack.append(int(token))
        
        return stack[0]