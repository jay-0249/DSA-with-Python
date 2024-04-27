class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ep1 = 0
        ep2 = len(height)-1
        def area(p1,p2):
            return (p2-p1)*(min(height[p1],height[p2]))
        maxWaterArea = 0
        while ep1 < ep2:
            currentWaterArea = area(ep1, ep2)
            if maxWaterArea<currentWaterArea:
                maxWaterArea = currentWaterArea
            if height[ep1]<height[ep2]:
                ep1 += 1
            else:
                ep2 -= 1
        return maxWaterArea
        
