class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        '''
        '''
        # Pair each car's position with its speed and sort by position descending
        cars = sorted(zip(position, speed), reverse=True)
        prevTimeTaken = -1
        fleetCount = 0
        
        for pos, spd in cars:
            # Calculate time for this car to reach the target without handling zero speed
            currentTime = float(target - pos) / spd
            
            #If current car can reach the destination even before the previous car, current car will have to meet previous car, form a fleet and proceed to reach destination
            if currentTime > prevTimeTaken:
                fleetCount += 1
                prevTimeTaken = currentTime
        
        # The number of elements in the stack represents the number of fleets
        return fleetCount
        