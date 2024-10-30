from collections import deque

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
        if not self.minStack or self.minStack[-1] > val:
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
        else:
            return
        

    def top(self):
        """
        :rtype: int
        """
        if self.mainStack:
            return self.mainStack[-1]
        else:
            return
        

    def getMin(self):
        """
        :rtype: int
        """
        if self.minStack:
            return self.minStack[-1]
        else:
            return


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()