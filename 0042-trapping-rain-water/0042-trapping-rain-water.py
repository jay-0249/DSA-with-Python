class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        '''
        Using two pointers
        have left max height, right max height
        at any random position, we can only store the water if the adjacent walls are more higher than this position.
        Let's iterate over the array using left and right pointers
        at each point of time, we have check which of the pointers is lower in height, bcz lower pointer decides the amount of water we can hold
        now if the lower bar is on the left side is lower than the left maximum wall, we can store some water above this left bar,
        else if the left bar is greater in height to that of left max, then update the left max
        similarly for the right bar 
        in this approach each other to find the water that can be trapped at each point of the array
        '''

        left, right = 0, len(height)-1
        left_max, right_max = height[left], height[right]
        vol_rain_water_trapped = 0

        while left < right:
            if height[left] < height[right]:
                if height[left] < left_max:
                    vol_rain_water_trapped += (left_max-height[left])
                else:
                    left_max = height[left]
                left += 1
            else:
                if height[right] < right_max:
                    vol_rain_water_trapped += (right_max-height[right])
                else:
                    right_max = height[right]
                right -= 1
            
        return vol_rain_water_trapped