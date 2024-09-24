class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        '''
        Brute Force Approach - Nested loops
        Run three nested loop.
        Time Complexity - O(N^3)
        Space Complexity - O(1)

        Optimised Brute Force Approach - Nested loop with hashing
        Hash all the numbers into default dictionary data structure using the collections library. Here each of the numbers of the array would be hashed as the key and their index would be appended into the list of values. (Here we are using defaultDict data structure as the number may be duplicated and so can have multiple indices in the array)
        Iterate over the array, at each iteration fix that number as the first number
        With the first number fixed, iterate over the array, at each iteration fix that number as the second number, see if there exists a number in the hash map with index not equal to that of the first and second number
        Time Complexity - O(N^2)
        Space Complexity - O(N)
        
        Break the 3 sum problem into iteration with 2 sum problem.
        Basically we can sort the numbers, then iterate over the array, in each iteration, we will fix that number as the middle number in the triplet and then we move the left and right to reach the target
        Time Complexity - O(NlogN)
        Space Complexity - O(1) assuming the sort is inplace sorting
        '''
        nums.sort()

        result = []
        if len(nums) < 3:
            return []
        
        for i,a in enumerate(nums):
            #skip all positive numbers, once you encounter a positive number
            if a>0:
                break
            #To avoid duplicates based on the first element
            if i>0 and a == nums[i-1]:
                continue
            #Find next two elements
            l,r = i+1,len(nums)-1
            while l<r:
                current_sum = a+nums[l]+nums[r]
                if current_sum > 0:
                    r -= 1
                elif current_sum < 0:
                    l += 1
                else:
                    result.append([a,nums[l],nums[r]])
                    #as we have made a pair with l,r positions, we have to modify l,r to find a new pair. Here if we change 'l', as 'a' is fixed it is sure that 'r' will also have to be modified 
                    l += 1
                    r -= 1
                    #to avoid duplicates caused
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
            
        return result
            
