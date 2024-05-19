class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        '''
        Intial thoughts:
           keyword -> Finding maximum number of consecutive -> subarray
           nums.length <= 10^5
           So our solution should O(N) or O(NlogN), but O(N^2)
           therefore we utilise Sliding window concept

        Solution:
            We will have to find a subarray i.e, window which is the maximum number of consective 1's in the binary array if you can flip at most k '0's
            The window is bounded by begin and end pointers
            Let's use a 'dictionary' data structure to store the elements we encounter and their respective frequency(number of times we encountered them) in the current window
            Start with element of the array, update the 'dictionary' data structure
            Check if we have zeroes more than k, if yes, we will have get rid of few zeroes to make our window a subarray that satisfies the given condition of atmost k '0's. So, we will move the begin pointer forward and update the 'dictionary' data structure by reducing the frequency of the element that begin pointer points to.
            Check if the current window length is more than the previous maximum length of such a window.
            Return the resultant maximum of lengths of suitable windows
        '''
        if k >= len(nums):
            return len(nums)

        maximumLength = 0
        numberOfZeroes = 0
        begin, end = 0, 0

        while end < len(nums):
            
            if nums[end] == 0:
                numberOfZeroes += 1
            
            end +=1

            while numberOfZeroes > k:

                if nums[begin] == 0:
                    numberOfZeroes -= 1
                
                begin += 1
            
            if end - begin > maximumLength and numberOfZeroes <= k:
                maximumLength = end-begin
            
        return maximumLength


        