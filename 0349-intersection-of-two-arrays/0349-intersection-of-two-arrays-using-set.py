class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        '''
        1st approach
        Sort both arrays
        Pick the smaller array, check each unique element of this array in the second array using binary search.

        Time Complexity - O(NlogN)+O(MlogM)+O(MlogN) ~ O(NlogN) where N is the length of the larger array
        Space Complexity - O(1)

        2nd approach
        We have to return only UNIQUE values of elements that are in both arrays
        So we can use set data structure to store each array in a set and find their intersection
        Time Complexity -> O(N+M) for creating sets, O(N)*O(1) for extracting intersection of the two sets. 
        Finally the time complexity is ~ O(N) where N is the size of the larger array
        Space Complexity -> O(N+M) for storing both arrays as sets
        Finally the space complexity is ~ O(N) where N is the size of the larger array
        '''
        setNums1 = set(nums1)
        setNums2 = set(nums2)
        #we can also & operator in place of intersection
        return setNums1 & setNums2
        #return setNums1.intersection(setNums2)