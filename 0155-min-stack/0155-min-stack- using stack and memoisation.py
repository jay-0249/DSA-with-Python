class MinStack(object):

    '''
    Here we have to implement a custom MinStack class.
    The push, pop, top operations can be performed in the order of O(1) time complexity with a stack.
    
    But how to implement a getMin() function that retrives the minimum of all the numbers at any point in the order of O(1) time complexity?

    what if we maintain another stack data structure whose top would always be the minimum of all the numbers inserted until now including the current number,
    if an element from main_stack is popped then the top of this min_stack will also be popped as the top of min_stack represents the min of all numbers in min_stack including the current number popped
    now the next top of min_stack would be the minimum of all the numbers in the main_stack currently 
    ...
    ...
    this way until when each element is popped from main_stack, the min_stack will also have to be popped so that the top of min_stack will be the minimum of all the numbers of main_stack at any point of time

    when a number is inserted, we can compare if it is less than minimum of previous numbers inserted. If yes, insert this number else insert the previous minimum. In this way we can calculate the minimum at each insert in O(1) time.

    similarly pop the min_stack when main_stack is popped
    '''

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        #calculate the minimum of the numbers with the current value included. This will be minimum of current value and previous minimum of all the numbers appended into the stack previously
        min_value_including_current_value = min(val, self.min_stack[-1] if self.min_stack else val)
        #understand the above calculation of min at each push operation with bottom to top approach, i.e, with just one or two elements to all elements
        self.min_stack.append(min_value_including_current_value)
        

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        #pop the minimum value as if of a window that contains all the numbers till & including the popped element
        self.min_stack.pop()
        #after the pop operation the top element of the min_stack would be the minimum of all the numbers in the stack

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()