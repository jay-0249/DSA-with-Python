from collections import deque
class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        '''
        #brute force - using nested loops - TLE
        Time Complexity - O(N^2)
        result = [0]*len(temperatures)
        for i,t in enumerate(temperatures):
            for j in range(i+1,len(temperatures)):
                if t < temperatures[j]:
                    result[i] = j-i
                    break
        return result
        '''
        stack = deque()
        result = [0]*len(temperatures)

        for i in range(0, len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                result[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
        
        return result


        