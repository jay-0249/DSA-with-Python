class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        speedDict = {position[i]:speed[i] for i in range(0, len(position))}
        position.sort(reverse = True)
        #print(speedDict)
        #print(position)
        fleetCount = 0
        i = 0
        
        while i < len(position):
            currentCar = position[i]
            #print(currentCar)
            currentSpeed = speedDict[currentCar]
            if currentSpeed == 0:
                if currentCar == target:
                    fleetCount += 1
                return fleetCount
            currentTime = float((target-currentCar))/currentSpeed
            j = i+1
            while j < len(position):
                nextCar = position[j]
                nextSpeed = speedDict[nextCar]
                if nextSpeed != 0:
                    nextTime = float((target-nextCar))/nextSpeed
                    #print("currentTime", currentTime)
                    #print("nextTime", nextTime)
                    if currentTime >= nextTime:
                        j += 1
                    else:
                        break
                else:
                    break
            #print(j)
            fleetCount += 1
            i = j
        
        return fleetCount
            
            

                
                
