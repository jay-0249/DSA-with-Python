from collections import deque
class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        '''
        # brute force - using nested loops - TLE
        Time Complexity - O(N^2)
        result = [0]*len(temperatures)
        for i,t in enumerate(temperatures):
            for j in range(i+1,len(temperatures)):
                if t < temperatures[j]:
                    result[i] = j-i
                    break
        return result

        # optimized approach
        store the indices of temperatures for which we haven't found warmer temperatures in a stack. 
        At each current temperature, we will check if for the days we stored in stack, the current temperature can be warmer temperature. 
        So the stack would be a monotonous decreasing stack, beacuse for any of the temperature if we found a higher temperature, 
        we will pop those out as we found warmer temperature for them.
        
        I am initialising result with zeroes before iteration, so if at all we do not find warmer temperature any temperature, 
        we do not have to enter zero after the iteration, rather it is already initialised
        Time Complexity - O(N)
        Space Complexity - O(N)
        '''
        stack = deque()
        result = [0]*len(temperatures)

        for i in range(0, len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                result[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
        
        return result


        
