class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        '''
        1st Approach - Not possible
        First I will check in a window of k+1 elements (index -> 0 to k) if there is a same element using XOR operator
        x^x = 0
        x^y != 0 unless x == y
        But if you operating XOR over more than two inputs, you could fail by detecting a set to contain duplicate even if it does not really contain a duplicate.
        Example (1,2,3)
        1^2^3 = (001)^(010)^(011) = (000) = 0
        The set (1,2,3) does not have any duplicates. But we misidentified it to contain a duplicate

        2nd Approach
        Iterate over the array, store the number and it's index as key-value pair respectively in a dictionary. 
        If such a number already exists in the dictionary, check if the index of that number currently - that of the same number in the dictionary <= k
        if yes, return true
        else update the index of the number in the dictionary with this number and continue 
        '''
        dictNumsIndex = dict()
        for i in range(0, len(nums)):
            prevIndex = dictNumsIndex.get(nums[i])
            if prevIndex is not None and (i-prevIndex<=k):
                return True
            else:
                dictNumsIndex[nums[i]] = i
                
        return False