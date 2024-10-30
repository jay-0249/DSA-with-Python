from collections import deque
'''
Brute Force:-
use minstack to store min value encountered until now. so at each time we insert a element, we insert the min value encountered until now.

Optimisation:- 
use minStack to store min value encountered until now. we can avoid storing min value for each node in stack to avoid duplicates until if the min number is encountered more than once. This will improve the space complexity in practical use.
'''
class MinStack(object):
    
    def __init__(self):
        self.stack = deque()
        self.minStack = deque() 

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        if not self.minStack or self.minStack[-1] >= val:
            self.minStack.append(val)

    def pop(self):
        """
        :rtype: None
        """
        if not self.stack:
            raise IndexError("We cannot Pop from empty stack")
        elif self.stack.pop() == self.minStack[-1]:
            self.minStack.pop()

   
    def top(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[-1]
        else:
            raise IndexError("Cannot fetch Top element from empty stack")
        
    def getMin(self):
        """
        :rtype: int
        """
        if self.minStack:
            return self.minStack[-1]
        else:
            raise IndexError("Cannot fetch minimum element for a empty stack")

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()