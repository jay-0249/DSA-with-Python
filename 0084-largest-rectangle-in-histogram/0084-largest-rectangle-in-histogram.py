from collections import deque
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        '''
        brute force
        for each rectangle bar, we have to find how much we can extend left and right with the same height.
        
        max_area = 0
 

        for i,h in enumerate(heights):
            if h > 0:
                current_area = h

                for j in range(i+1, len(heights)):
                    if h > heights[j]:
                        break
                    else:
                        current_area += h
                
                for j in range(i-1,-1,-1):
                    if h > heights[j]:
                        break
                    else:
                        current_area += h

                if max_area < current_area:
                    max_area = current_area
        
        return max_area
        '''
        maxArea = 0
        stack = []

        for i,h in enumerate(heights):
            #Either Stack is empty or we had come across a lesser height than before
            if stack and stack[-1][1]>h:
                start = 0
                while stack and stack[-1][1]>h:
                    index, height = stack.pop()
                    maxArea = max(maxArea, height*(i-index))
                    start = index
                stack.append((start, h))
            else:
                stack.append((i,h))

        while stack:
            index, height = stack.pop()
            maxArea = max(maxArea, height*(len(heights)-index))

        return maxArea