class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        '''
        Sort both arrays
        Pick the smaller array, check each unique element of this array in the second array using binary search.

        Time Complexity - O(NlogN)+O(MlogM)+O(MlogN)
        Space Complexity - O(1)
        '''

        #sort both arrays
        nums1.sort()
        nums2.sort()
        
        #Iterate over the smaller array and check if each unique number of the smaller array is present in the larger array. Binary Search is used to search.
        def binarySearch(num, numsArr):
            l, r = 0, len(numsArr)-1

            while l<=r:
                mid = l+(r-l)/2
                if num == numsArr[mid]:
                    return True
                elif num < numsArr[mid]:
                    r = mid-1
                else:
                    l = mid+1
            
            return False
        
        prevNum = None
        intersectionOfArrays = []
        #Shallow copy of an array will not create another copy of that array rather will also point to the same array
        largerArray = copy.copy(nums1)
        smallerArray = copy.copy(nums2)
        if len(nums1) < len(nums2):
            largerArray = copy.copy(nums2)
            smallerArray = copy.copy(nums1)
        
        for i in range(0,len(smallerArray)):
            currNum = smallerArray[i]
            print(currNum, binarySearch(currNum,largerArray))
            if currNum != prevNum and binarySearch(currNum,largerArray):
                intersectionOfArrays.append(currNum)
            prevNum = smallerArray[i]

        return intersectionOfArrays

