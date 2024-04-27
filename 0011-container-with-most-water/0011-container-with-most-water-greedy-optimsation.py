class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        '''
        Let's use two pointers to indicate two walls
        Let's go with greedy approach to find the max area, i.e, at an iteration after checking if the area between the walls with maximum area we had before, of the two walls we continue with the wall with more height while we move to the next wall that is next to the smaller wall
        Each starting this iteration over the array, we will fetch the maximum height of the wall. At each iteration we will check the maximum area vs an area of between walls as if the walls of the maximum height.
        If maximum area we have visited > maximum wall height * (left wall index - right wall index), then there is no chance that we will find an area greater to max area. It is because the maximum height of all walls is same always and the difference between left and right walls index keep shrinking. So it is better to break and return the maximum area
        This way we will iterate over the array
        '''
        ep1 = 0
        ep2 = len(height)-1
        maxArea = 0
        maxHeightOfAllWalls = max(height)
        while ep1 < ep2:
            currentArea = (ep2-ep1)*(min(height[ep1],height[ep2]))
            if maxArea<currentArea:
                maxArea = currentArea
                if maxHeightOfAllWalls*(ep2-ep1) < currentArea:
                    return maxArea     
            if height[ep1]<height[ep2]:
                ep1 += 1
            else:
                ep2 -= 1
        return maxArea
        