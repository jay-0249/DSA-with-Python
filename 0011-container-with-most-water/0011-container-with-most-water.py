class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        '''
        Bruteforce Approach - nested loop
            Iterate over the array, for each iteration fix that number as the first wall and then iterate over the rest of array to find a wall that can be the second wall, such that the volume is maximised. In each iteration, update the maximum volume of the container.
            Time Complexity - O(N^2)
            Space Complexity - O(1)
        
        maxVolume = 0    
        for i in range(0,len(height)-1):
            for j in range(i+1,len(height)):
                currentVolume = abs((j-i)*(min(height[j],height[i])))
                maxVolume = max(maxVolume, currentVolume)
        return maxVolume 

        Greedy Approach - Two Pointers
        The basic underlying idea is that at each point of time, I want to to move to a bigger container possible locally.
        First using two pointers from left and right side of the array. Now that you have a container, check if the volume is greater than max volume, if not update it.
        Then, the wall that is the smaller wall, move to another wall
        '''
        maxVolume = 0
        l, r = 0,len(height)-1
        while l < r:
            currentVolume = abs((r-l)*(min(height[l],height[r])))
            maxVolume = max(maxVolume, currentVolume)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return maxVolume