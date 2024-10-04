class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        def is_token_int(token):
            is_int = True
            try:
                result = int(token)
            except ValueError:
                is_int = False
            return is_int

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
            elif is_token_int(token):
                stack.append(int(token))
            else:
                return -1
        
        
        if not stack:
            return 0
        else:
            return stack[0]