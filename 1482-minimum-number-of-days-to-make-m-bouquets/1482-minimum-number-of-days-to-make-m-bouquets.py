class Solution(object):
    def minDays(self, bloomDay, m, k):
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
        #we need a minimum of m*k flowers to make m bouquets each of k flowers
        if len(bloomDay) < m*k:
            return -1
        
        #if we have enough flowers they will have to bloom some or the other day
        #so in the worst case the minimum number of days required would be the maximum of blooming days and the best case would be the minimum of blooming days
        maxBloomDay = max(bloomDay)
        minBloomDay = min(bloomDay)

        #Now that we have a range for minimum number of days required [minBloomDay, maxBloomDay] 
        #If we form a list of the number of bouquets by a given day for each day in this range, it will be in a non-decreasing order
        #so this means this list of the number of bouquets by a given day is a sorted list and the min number of days is also a range
        #so we can search in this range using a binary search, and calculate the number of bouquets by a given day and find the minimum number of days required to make m bouquets

        minDaysRequired = maxBloomDay
        
        while minBloomDay <= maxBloomDay:
            mid = minBloomDay + (maxBloomDay - minBloomDay)//2
            numOfBouquetsMade = 0
            #helper Function to find numOfBouquetsMade
            #iterate over the bloomDay array to find number of adjacent flowers bloomed and there by available to make a bouquet
            numOfFlowersAvailable = 0
            for f in bloomDay:
                #if the blooming day is less than or same as the current day, then we can use this flower to make a bouquet
                if f <= mid:
                    numOfFlowersAvailable += 1
                    if numOfFlowersAvailable == k:
                        numOfFlowersAvailable = 0
                        numOfBouquetsMade += 1
                #if the blooming day is greater than the current day, then we can not yet use this flower to make a bouquet, so the previous adjacent flowers cannot yet be used to make a bouquet if there any left 
                else:
                    numOfFlowersAvailable = 0
            
            if numOfBouquetsMade >= m:
                minDaysRequired = mid
                maxBloomDay = mid-1
            else:
                minBloomDay = mid+1
        
        return minDaysRequired


        
        