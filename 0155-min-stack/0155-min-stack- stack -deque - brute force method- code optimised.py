from collections import deque
'''
Brute Force:-
use minstack to store min value encountered until now. so at each time we insert a element, we insert the min value encountered until now.

Optimisation:- 
use minStack to store min value encountered until now. we can avoid storing min value for each node in stack to avoid duplicates until if the min number is encountered more than once. This will improve the space complexity in practical use.
'''
class MinStack(object):
    
    def __init__(self):
        self.mainStack = deque()
        self.minStack = deque() 

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.mainStack.append(val)
        if not self.minStack or self.minStack[-1] >= val:
            self.minStack.append(val)
        else:
            self.minStack.append(self.minStack[-1])

    def pop(self):
        """
        :rtype: None
        """
        if self.mainStack:
            self.minStack.pop()
            return self.mainStack.pop()
   
    def top(self):
        """
        :rtype: int
        """
        if self.mainStack:
            return self.mainStack[-1]
        
    def getMin(self):
        """
        :rtype: int
        """
        if self.minStack:
            return self.minStack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()