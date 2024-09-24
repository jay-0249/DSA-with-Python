class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        '''
        Brute Force - Using nested loop
            For each number, we will see if we can find a number such that the sum equals the target

            Time Complexity - O(N^2)
            Space Complexity - O(1)

        Approach 2 - using hashing
            Let's hash all the numbers in the array into a hash set
            Now iterate over the array to see if there exists a number in the hashset such that the sum equals the target
            
            Time Complexity - O(N)
            Space Complexity - O(N) - Doesn't satisfy our question requirements
            In this approach, we are not taking advantage of the sorted nature of the array
        
        Approach 3 - using Two Pointer approach
            We already know that the array is sorted in non-decreasing order, let's use this fact, try to create a sum of a number from start and end of the array.
            Now if this sum is less than that of the target, we understand that we have increase the sum, so we can move the number from the start side of the array to it's adjacent number as it is bigger. In this way we can move the index from the start side of the array, to increase the sum and eventually try to match with the target sum
            Similary if the sum is greater than the target, we can move the index from the end side of the array to find a smaller number and decrease the sum to match with that of the target.
            You may ask why not move the index on the start side to find a smaller number, but actually we have tried that number before coming to this number and given that our question mentions that we have only one solution for a test case. We do not have to worry about it.
            Time Complexity - O(N)
            Space Complexity  - O(1)
        '''
        l = 0
        r = len(numbers) - 1
        #l,r travel towards eachother so we do not require additional condiations over the bounds of l,r
        while l < r:
            sum = numbers[l]+numbers[r]
            if sum == target:
                return [l+1,r+1]
            elif sum < target:
                l += 1
            else:
                r -= 1
        
            