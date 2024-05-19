class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        '''
        Find the maximum sum of contiguous subarray of k elements
        Then return its average

        For finding the maximum sum of subarray with k elements, use the sliding window method. That is, take the subarray with first k elements, calculate it's sum. 
        Now, the simplest immediate subarray would be to modify this subarray to include k+1 th element and remove the 1st element of the subarray.
        Similarly, we can proceed to create a new subarray by modifying the current subarray, by adding the element next to the current sub array and removing the first element of the first subarray.
        We can proceed to go on creating such subarrays until we do not have a new element next to the last element.
        If we observe this we are sliding a window encompassing the subarray over the array, to create new subarrays. And so this technique is called Sliding Window
        We can find the sum of new array using current subarray, just like we create new subarray using the existing subarray by adding the element next to the current subarray and remove the first element of the subarray.

        In this approach we iterate over the whole array just once, so the time complexity is linear.
        Time Complexity -> O(N)
        Space Complexity -> O(1)
        '''

        currentSubarraySum = 0
        #Find the sum of first contiguous subarray consisting of first k elements
        for i in range(0,k):
            currentSubarraySum += nums[i]

        maximumSubarraySum = currentSubarraySum
        #Slide over the array
        for i in range(k,len(nums)):
            currentSubarraySum += nums[i] - nums[i-k]
            if maximumSubarraySum < currentSubarraySum:
                maximumSubarraySum = currentSubarraySum
        
        #Find the average and round the average to 5 decimals
        #Adding float to the numerator is important as to avoid the divison return just a integer without the decimal part of the divison result
        
        #maxContiguousSubarrayAverage = round(float(maximumSubarraySum)/k, 5)

        return round(float(maximumSubarraySum)/k, 5)
        